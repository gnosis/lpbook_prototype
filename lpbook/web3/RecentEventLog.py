import logging
from typing import Any, List

from web3.types import HexBytes

from lpbook import CacheMissError

from .EventNotifier import EventNotifier

logger = logging.getLogger(__name__)

class RecentEventLog:
    """"Stores events from a start block up to the most recent block.
    """
    def __init__(self, lp_ids, event_types, web3_client, block_index):
        self.web3_client = web3_client
        self.event_types = event_types
    
        self.events = []
        self.start_block_number = None
        self.start_block_hash = None
        
        self.lp_ids = lp_ids
        self.block_index = block_index
        self.block_index.subscribe_to_new_blocks(self.update_event_notifier)


    def create_event_notifier(self, lp_ids):
        self.event_notifier = EventNotifier(
            self.event_callback,
            self.event_types,
            [self.web3_client.toChecksumAddress(lp_id.lower()) for lp_id in lp_ids],
            self.web3_client
        )

    async def update_event_notifier(self, block_number, block_hash):
        if self.start_block_number is None:
            self.start_block_number = block_number
            self.start_block_hash = block_hash

        logger.debug(f"Polling blockchain for new events {self} ...")
        await self.event_notifier.update()
        logger.debug(f"Polling blockchain for new events {self} ... done")

    def is_ready(self):
        return self.start_block_number is not None

    def event_callback(self, event):
        logger.debug(f"Got event: {event}.")

        assert \
            len(self.events) == 0 or \
            event.blockNumber > self.events[-1].blockNumber or \
            (event.blockNumber == self.events[-1].blockNumber and event.logIndex > self.events[-1].logIndex) or \
            event.removed

        if event.removed:
            # If it is removed, then we must have it stored.
            assert len(self.events) > 0
            self.events = [
                e for e in self.events
                if e.blockHash != event.blockHash or e.logIndex != event.logIndex
            ]
        else:
            assert \
                len(self.events) == 0 or \
                event.blockNumber > self.events[-1].blockNumber or \
                (event.blockNumber == self.events[-1].blockNumber and event.logIndex > self.events[-1].logIndex)
            self.events.append(event)

            # This can happen if all events are removed
            if event.blockNumber < self.start_block_number:
                self.start_block_number = event.blockNumber
                self.start_block_hash = event.blockHash.hex()

    def start(self, from_block_number: int = None) -> None:
        """Sets start_block to given block and starts collecting the delta asynchronously.

        If from_block_number is None, then it is set to the most recent block.

        Note: If there is a reorg and start_block becomes orphan, then start_block will be
        reset to oldest block of the sequence that is added to the active chain.
        """
        logger.debug(f"Starting {self}")
        #if from_block_number is None:
        #    from_block_number = 'latest'
        #start_block = self.web3_client.eth.get_block(from_block_number)
        #self.start_block_number = start_block.number
        #self.start_block_hash = start_block.hash.hex()

        self.create_event_notifier(self.lp_ids)
        self.event_notifier.start(from_block_number)

    def stop(self) -> None:
        self.event_notifier.stop()
        self.start_block_number = self.start_block_hash = None

    def replace_lps(self, new_lp_ids):
        """Replaces the recent set of monitored lp addresses."""
        self.stop()
        self.create_event_notifier(new_lp_ids)
        self.start()

    def get_block_number_from_block_hash(self, block_hash):
        i = self.block_hashes.index(block_hash)
        return self.block_numbers[i]

    def __call__(self, block_number=None, block_hash=None) -> List[Any]:
        """Returns deltas from self.get_start_block() up to (including) given block.

        If block is given but not cached, will raise a CacheMissError.
        Note: the block range for which deltas are returned is [start_block, block].
        """
        if block_hash is not None:
            if block_hash not in self.block_index.block_hashes:
                raise CacheMissError(f"No events for block {block_hash} in cache.")
            block_number = self.block_index.get_block_number_from_hash(block_hash)
        if block_number is not None:
            if block_number not in self.block_index.block_numbers:
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
