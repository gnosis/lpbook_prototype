import logging
from abc import abstractmethod
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional

from async_timeout import asyncio
from eth_utils import event_abi_to_log_topic
from lpbook.util import traced
from lpbook.web3 import BlockId
from lpbook.web3.block_stream import BlockScanning

from web3._utils.events import get_event_data
from web3._utils.filters import Filter
from web3.contract import ContractEvent
from web3.datastructures import AttributeDict
from web3.exceptions import MismatchedABI

logger = logging.getLogger(__name__)


class EventStream:
    """Defines a pub/sub interface for a web3 stream of events."""
    Subscriber = Callable[[int, str], None]

    @abstractmethod
    def subscribe(
        self,
        subscriber: Subscriber,
        addresses: List[str],
        events: List[ContractEvent],
        from_block_number: Optional[int],
        on_dropped_subscription_error_fn: Callable[[RuntimeError], None]
    ):
        """Subscribes the event stream filtered for given addresses and events.

        Subscriber is called only for events that match one of the given addresses AND
        one of the given events.

        Passing an empty list of addresses will call subscriber on any address.
        The list of events must have at least one event.
        """

    @abstractmethod
    def unsubscribe(self, subscriber: Subscriber):
        """Stops calling subscriber."""

    @abstractmethod
    def change_subscription(
        self,
        subscriber: Subscriber,
        addresses: List[str],
        events: List[ContractEvent],
        from_block_number: Optional[int]
    ):
        """Changes what subscriber subscribes to."""


class DroppedSubscriptionError(RuntimeError):
    """Signals that subscription was dropped by the node."""
    # Apparently it does not annoy anyone in the blockchain world.


def raise_err(err):
    raise err


class ServerFilteredEventPollingStream(EventStream):
    """A stream of events that is filtered on the server (the web3 node).

    Creates server side filters to minimize the amount of data transferred,
    at the cost of potentially larger number of calls to the node
    (one for every subscriber for every block).

    NOTE: No effort is done to try to merge equivalent subscriptions for multiple
    subscribers - it is expected that clients of this class will do that if required.
    """

    @dataclass
    class Subscription:
        addresses: List[str]
        events: List[ContractEvent]
        filter: Filter
        updated_once: bool = False,
        on_dropped_subscription_error_fn: Callable[[RuntimeError], None] = raise_err

    def __init__(self, web3_client):
        self.web3_client = web3_client
        self.subscriptions = {}

    def subscribe(
        self,
        subscriber: EventStream.Subscriber,
        addresses: List[str],
        events: List[ContractEvent],
        from_block_number: Optional[int],
        on_dropped_subscription_error_fn: Callable[[RuntimeError], None]
    ):
        assert len(events) > 0
        filter = self.install_filter(addresses, events, from_block_number)
        subscription = self.Subscription(
            addresses, events, filter, False, on_dropped_subscription_error_fn
        )
        self.subscriptions[subscriber] = subscription

    def change_subscription(
        self,
        subscriber: EventStream.Subscriber,
        addresses: List[str],
        events: List[ContractEvent],
        from_block_number: Optional[int]
    ):
        assert len(events) > 0
        self.unsubscribe(subscriber)
        self.subscribe(subscriber, addresses, events, from_block_number)

    def unsubscribe(self, subscriber: EventStream.Subscriber):
        subscription = self.subscriptions[subscriber]
        self.uninstall_filter(subscription.filter)
        self.subscriptions.pop(subscriber)

    async def poll_for_subscriber_helper(
        self,
        subscriber: EventStream.Subscriber
    ):
        subscription = self.subscriptions[subscriber]

        filter = subscription.filter

        if subscription.updated_once:
            new_entries = await asyncio.to_thread(filter.get_new_entries)
        else:
            new_entries = await asyncio.to_thread(filter.get_all_entries)

        decoded_events = []
        for encoded_event in new_entries:
            decoded_event = None
            for event in subscription.events:
                event_abi = event._get_event_abi()
                try:
                    decoded_event = get_event_data(
                        self.web3_client.codec,
                        event_abi,
                        encoded_event
                    )
                except MismatchedABI:
                    pass
            decoded_event = AttributeDict(
                decoded_event,
                removed=encoded_event.removed
            )
            assert decoded_event is not None
            decoded_events.append(decoded_event)

        subscription.updated_once = True

        # Apparently node will always send us the events in the
        # "right" order.

        decoded_events = sorted(
            decoded_events,
            key=lambda e: (not e.removed, e.blockNumber, e.logIndex)
        )

        for decoded_event in decoded_events:
            subscriber(decoded_event)

    async def poll_for_subscriber(
        self,
        subscriber: EventStream.Subscriber
    ):
        try:
            return await self.poll_for_subscriber_helper(subscriber)

        # sometimes the node just drops the filter without notice :(
        except ValueError as err:
            if self.is_filter_not_found_error(err):
                self.subscriptions[subscriber].on_dropped_subscription_error_fn(
                    DroppedSubscriptionError()
                )
            else:
                raise err

    @traced(logger, 'Polling blockchain for new events')
    async def poll(self, *args, **kwargs):
        await asyncio.gather(*[
            self.poll_for_subscriber(subscriber)
            for subscriber in self.subscriptions.keys()
        ])

    def get_event_as_topic(self, event):
        return '0x' + event_abi_to_log_topic(event._get_event_abi()).hex()

    def install_filter(self, addresses, events, from_block_number: Optional[int]):
        event_signature_hashes = [
            self.get_event_as_topic(event) for event in events
        ]

        filter_parameters = {}
        if len(addresses) > 0:
            filter_parameters['address'] = [
                self.web3_client.toChecksumAddress(address.lower())
                for address in addresses
            ]
        filter_parameters['topics'] = [event_signature_hashes]
        if from_block_number is not None:
            filter_parameters['fromBlock'] = from_block_number

        return self.web3_client.eth.filter(filter_parameters)

    def is_filter_not_found_error(self, error):
        return error.args[0]["code"] == -32000

    def uninstall_filter(self, filter):
        try:
            self.web3_client.eth.uninstall_filter(filter.filter_id)
        # sometimes the node just drops the filter without notice :(
        except ValueError as err:
            if not self.is_filter_not_found_error(err):
                raise err

    def unsubscribe_all(self):
        for subscription in self.subscriptions.values():
            self.uninstall_filter(subscription.filter)
        self.subscriptions = {}


class ServerFilteredEventStream(ServerFilteredEventPollingStream, BlockScanning):
    def __init__(self, block_stream, web3_client):
        ServerFilteredEventPollingStream.__init__(self, web3_client)
        self.block_stream = block_stream
        self.block_stream.subscribe(self.poll)

    @property
    def last_block(self) -> Optional[BlockId]:
        return self.block_stream.last_block

