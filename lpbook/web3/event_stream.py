from abc import abstractmethod
from dataclasses import dataclass
import logging

from typing import Dict, List, Callable
from async_timeout import asyncio

from web3._utils.events import get_event_data
from web3._utils.filters import Filter
from web3.datastructures import AttributeDict
from web3.contract import ContractEvent
from lpbook.util import traced

from lpbook.web3 import BlockDescriptor
from lpbook.web3.block_stream import BlockScanning

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
        from_block: BlockDescriptor
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
        from_block_number: BlockDescriptor
    ):
        """Changes what subscriber subscribes to."""


def get_event_signature(event):
    event = event._get_event_abi()
    return f"{event['name']}({','.join(input['type'] for input in event['inputs'])})"


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
        filters: Dict[ContractEvent, Filter]
        updated_once: bool = False

    def __init__(self, web3_client):
        self.web3_client = web3_client
        self.subscriptions = {}

    def subscribe(
        self,
        subscriber: EventStream.Subscriber,
        addresses: List[str],
        events: List[ContractEvent],
        from_block: BlockDescriptor
    ):
        assert len(events) > 0
        filters = {}
        for event in events:
            filter = self.install_filter(addresses, event, from_block)
            filters[event] = filter
        subscription = self.Subscription(addresses, events, filters, False)
        self.subscriptions[subscriber] = subscription

    def change_subscription(
        self,
        subscriber: EventStream.Subscriber,
        addresses: List[str],
        events: List[ContractEvent],
        from_block: BlockDescriptor
    ):
        assert len(events) > 0
        self.unsubscribe(subscriber)
        self.subscribe(subscriber, addresses, events, from_block)

    def unsubscribe(self, subscriber: EventStream.Subscriber):
        subscription = self.subscriptions[subscriber]
        for filter in subscription.values():
            self.uninstall_filter(filter)
        self.subscriptions.pop(subscription)

    @traced(logger, 'Polling blockchain for new events')
    async def poll(self, block_number: int, block_hash: str):
        for subscriber, subscription in self.subscriptions.items():
            decoded_events = []
            for event, filter in subscription.filters.items():
                if subscription.updated_once:
                    new_entries = await asyncio.to_thread(filter.get_new_entries)
                else:
                    new_entries = await asyncio.to_thread(filter.get_all_entries)
                for encoded_event in new_entries:
                    event_abi = event._get_event_abi()
                    decoded_event = get_event_data(
                        self.web3_client.codec,
                        event_abi,
                        encoded_event
                    )
                    decoded_event = AttributeDict(
                        decoded_event,
                        removed=encoded_event.removed
                    )
                    decoded_events.append(decoded_event)
            subscription.updated_once = True
            decoded_events = sorted(
                decoded_events,
                key=lambda e: (e.blockNumber, e.logIndex)
            )
            for decoded_event in decoded_events:
                subscriber(decoded_event)

    def get_event_signature_hash(self, event):
        return self.web3_client.keccak(text=get_event_signature(event)).hex()

    def install_filter(self, addresses, event, from_block: BlockDescriptor):
        event_signature_hash = self.get_event_signature_hash(event)

        filter_parameters = {}
        if len(addresses) > 0:
            filter_parameters['address'] = [
                self.web3_client.toChecksumAddress(address.lower())
                for address in addresses
            ]
        filter_parameters['topics'] = [event_signature_hash]
        if from_block is not None:
            filter_parameters['fromBlock'] = from_block
        return self.web3_client.eth.filter(filter_parameters)

    def uninstall_filter(self, filter):
        self.web3_client.eth.uninstall_filter(filter.filter_id)

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
    def last_block_number(self) -> int:
        return self.block_stream.last_block_number

    @property
    def last_block_hash(self) -> str:
        return self.block_stream.last_block_hash
