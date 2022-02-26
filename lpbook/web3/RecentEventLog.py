import logging
from typing import Any, List

from lpbook.error import CacheMissError

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
        self.start_block_hash = None

    def process_new_event(self, event):
        logger.debug(f"Processing event {event} ....")

        assert \
            len(self.events) == 0 or \
            event in self.events or \
            event.blockNumber > self.events[-1].blockNumber or \
            (event.blockNumber == self.events[-1].blockNumber and event.logIndex > self.events[-1].logIndex) or \
            event.removed

        if event.removed and event in self.events:
            self.events = [
                e for e in self.events
                if e.blockHash != event.blockHash or e.logIndex != event.logIndex
            ]
        elif event not in self.events:
            assert \
                len(self.events) == 0 or \
                event.blockNumber > self.events[-1].blockNumber or \
                (event.blockNumber == self.events[-1].blockNumber and event.logIndex > self.events[-1].logIndex)
            self.events.append(event)

            # This could happen if all events are removed. To avoid it, pass an old enough from_block 
            # to the "start" method.
            if event.blockNumber < self.start_block_number:
                logger.critical(f'{self} found in an possibly inconsistent state. Exiting ...')
                assert False

    def start(
        self,
        addresses: List[str],
        events: List[ContractEvent],
        start_block_number: int,
        start_block_hash: str,
    ) -> None:
        """Sets start_block to given block and starts collecting the delta asynchronously.

        NOTE: start_block must be old enough so that if there is a reorg it can't become
        orphan. There are some efforts to detect this case, but they are not complete.
        """
        self.start_block_number = start_block_number
        self.start_block_hash = start_block_hash
        logger.debug(f"Starting {self} ...")
        self.event_stream.subscribe(
            self.process_new_event,
            addresses,
            events,
            start_block_number
        )

    def stop(self) -> None:
        self.event_stream.unsubscribe(self.process_new_event)
        self.start_block_number = self.start_block_hash = None
        logger.debug('Stopped {self}')

    def update(self, addresses: List[str], events: List[ContractEvent]):
        """Updates filter."""
        logger.debug(f'Updating {self} ...')

        cur_block_hash = self.event_stream.last_block_hash

        # NOTE: we can do this since process_event above ensures de-duplication of events.
        # The cur_block_number + 1 alternative does not look robust to race
        # conditions due to chain reorgs.
        self.event_stream.change_subscription(self.process_new_event, addresses, events, cur_block_hash)

    def __call__(self, block_number=None, block_hash=None) -> List[Any]:
        """Returns deltas from self.get_start_block() up to (including) given block.

        If block is given but not cached, will raise a CacheMissError.
        Note: the block range for which deltas are returned is [start_block, block].
        """
        if block_hash is not None:
            if block_hash not in self.event_stream.block_hashes:
                raise CacheMissError(f"No events for block {block_hash} in cache.")
            block_number = self.event_stream.get_block_number_from_hash(block_hash)
        if block_number is not None:
            if block_number not in self.event_stream.block_numbers:
                raise CacheMissError(f"No events for block {block_number} in cache.")
            return [e for e in self.events if e.blockNumber <= block_number]
        return self.events

    @property
    def block_count(self) -> int:
        """Get number of blocks in the log."""
        if len(self.events) == 0:
            return 0
        return self.events[-1].blockNumber - self.events[0].blockNumber + 1

    def update_start_block(self, new_start_block_number) -> None:
        """Updates start block monotonically.

        Updates start block to more recent block. This will free
        all delta between start_block and new_start_block - 1.

        PRE: new_start_block >= self.start_block()
        POST: self.start_block() >= new_start_block
        """
        self.events = [e for e in self.events if e.blockNumber >= new_start_block_number]
        assert len(self.events) > 0
        self.start_block_number = self.events[0].blockNumber
        self.start_block_hash = self.events[0].blockHash.hex()
