import logging
from typing import Any, List

from lpbook.error import CacheMissError
from lpbook.util import traced

from .event_stream import EventStream
from web3.contract import ContractEvent

logger = logging.getLogger(__name__)


class RecentEventLog:
    """"Stores events from a start block up to the most recent block.

    Keeps events sorted, taking care of potential chain reorgs.
    """
    def __init__(self, web3_client, event_stream: EventStream):
        self.web3_client = web3_client
        self.event_stream = event_stream

        self.events = []
        self.start_block_number = None

    def process_new_event(self, event):
        logger.debug(f'Processing event {event} ...')

        print(event.removed)
        print(len(self.events))
        print(event.blockNumber)
        print(event.logIndex)
        if len(self.events) > 0:
            print(self.events[-1].blockNumber)
            print(self.events[-1].logIndex)

        assert \
            len(self.events) == 0 or \
            event in self.events or \
            event.blockNumber > self.events[-1].blockNumber or \
            (
                event.blockNumber == self.events[-1].blockNumber and
                event.logIndex > self.events[-1].logIndex
            ) or \
            event.removed

        if event.removed:
            self.events = [
                e for e in self.events
                if e.blockHash != event.blockHash or e.logIndex != event.logIndex
            ]
        elif event not in self.events:
            assert \
                len(self.events) == 0 or \
                event.blockNumber > self.events[-1].blockNumber or \
                (
                    event.blockNumber == self.events[-1].blockNumber and
                    event.logIndex > self.events[-1].logIndex
                )

            self.events.append(event)

            # This could happen if all events are removed. To avoid it, pass an old enough
            # from_block to the "start" method.
            if event.blockNumber < self.start_block_number:
                print(event.blockNumber)
                print(self.start_block_number)
                logger.critical(
                    f'{self} found in an possibly inconsistent state. Exiting ...'
                )
                assert False

    @traced(logger, 'Starting RecentEventLog')
    async def start(
        self,
        addresses: List[str],
        events: List[ContractEvent],
        start_block_number: int
    ) -> None:
        """Sets start_block to given block and starts collecting the delta asynchronously.

        NOTE: start_block must be old enough so that if there is a reorg it can't become
        orphan. There are some efforts to detect this case, but they are not complete.
        """
        print(f'Start block number is {start_block_number}')
        self.start_block_number = start_block_number
        self.event_stream.subscribe(
            self.process_new_event,
            addresses,
            events,
            start_block_number
        )
        await self.event_stream.poll_for_subscriber(self.process_new_event)

    def stop(self) -> None:
        self.event_stream.unsubscribe(self.process_new_event)
        self.start_block_number = None
        logger.debug('Stopped {self}')

    def update(self, addresses: List[str], events: List[ContractEvent]):
        """Updates filter."""
        logger.debug(f'Updating {self} ...')

        cur_block_hash = self.event_stream.last_block_hash

        # NOTE: we can do this since process_event above ensures de-duplication of events.
        # The cur_block_number + 1 alternative does not look robust to race
        # conditions due to chain reorgs.
        self.event_stream.change_subscription(
            self.process_new_event,
            addresses,
            events,
            cur_block_hash
        )

    def __call__(self, block_number=None, block_hash=None) -> List[Any]:
        """Returns deltas from self.get_start_block() up to (including) given block.

        If block is given but not cached, will raise a CacheMissError.
        Note: the block range for which deltas are returned is [start_block, block].
        """
        if block_hash is not None:
            block_number = self.web3_client.eth.get_block(block_hash).number
        if block_number is not None:
            if block_number < self.start_block_number or \
               block_number > self.event_stream.last_block_number:
                raise CacheMissError(f'No events for block {block_number} in cache.')
            return [e for e in self.events if e.blockNumber <= block_number]
        return self.events

    @property
    def block_count(self) -> int:
        """Get number of blocks in the log."""
        return self.event_stream.last_block_number - self.start_block_number + 1

    def update_start_block(self, new_start_block_number) -> None:
        """Updates start block monotonically.

        Updates start block to more recent block. This will free
        all delta between start_block and new_start_block - 1.

        PRE: new_start_block >= self.start_block()
        POST: self.start_block() >= new_start_block
        """
        self.events = [e for e in self.events if e.blockNumber >= new_start_block_number]
        self.start_block_number = new_start_block_number
