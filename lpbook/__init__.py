import asyncio
from enum import Enum
import logging
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Union

from lpbook.util import LP
from lpbook.web3 import Block
from lpbook.web3.block_stream import BlockStream
from lpbook.web3.RecentEventLog import RecentEventLog
from lpbook.error import CacheMissError

logger = logging.getLogger(__name__)



class RecentStateCache:
    def __init__(self, cache_size):
        self.recent_block_hashes = []
        self.recent_block_numbers = []
        self.state_by_block_hash = {}
        self.cache_size = cache_size

    def get_block_hash(self, block_number: int) -> str:
        try:
            i = self.recent_block_numbers.index(block_number)
        except ValueError:
            raise CacheMissError(f'Could not find block {block_number} in recent state cache.')
        return self.recent_block_hashes[i]

    def get_at_block_number(self, block_number: int) -> Any:
        return self.state_by_block_hash[self.get_block_hash(block_number)]

    def get_at_block_hash(self, block_hash: str) -> Any:
        try:
            return self.state_by_block_hash[block_hash]
        except KeyError:
            raise CacheMissError(f'Cound not find block {block_hash} in recent state cache.')

    def get_at_block(self, block_number: int = None, block_hash: str = None) -> Any:
        """Returns the state at block if given, otherwise return most recently added."""
        if block_hash is not None:
            return self.get_at_block_hash(block_hash)
        elif block_number is not None:
            return self.get_at_block_number(block_number)
        return self.get_most_recently_added()

    def get_most_recently_added(self) -> Any:
        if len(self.recent_block_hashes) == 0:
            raise CacheMissError(
                f'Attempt to retrieve most recently added state from an empty {self}.'
            )
        return self.state_by_block_hash[self.recent_block_hashes[-1]]

    def add(self, block_number: int, block_hash: str, state) -> None:
        self.recent_block_numbers.append(block_number)
        self.recent_block_hashes.append(block_hash)
        self.state_by_block_hash[block_hash] = state
        # Keep cache maximum size.
        if len(self.recent_block_numbers) > self.cache_size:
            assert len(self.recent_block_numbers) == self.cache_size + 1
            self.state_by_block_hash.pop(self.recent_block_hashes[0])
            self.recent_block_hashes = self.recent_block_hashes[1:]
            self.recent_block_numbers = self.recent_block_numbers[1:]


class LPAsyncProxy(ABC):
    """Asynchronous proxy to a collection of LP states indexed by block number/hash .

    Accessing states through this class usually implies a, possibly slow,
    call to the proxied data source.
    """
    @abstractmethod
    async def __call__(self, block_number=None, block_hash=None) -> Dict[str, LP]:
        """Returns a dictionary of LP states indexed by their LP id, at given block."""

    @abstractmethod
    async def latest_block(self) -> Block:
        """Returns the block of the latest state in the collection."""


class LPSyncProxy(ABC):
    """Synchronous proxy to a collection of LP states indexed by block number/hash .

    This proxy will be kept synchronized with the proxied data structure. Accessing state
    through this class will either be quick, or raise an error if the proxy is out of sync.
    """
    @abstractmethod
    def __call__(self, block_number: int = None) -> Dict[str, LP]:
        """Returns the recent state if synced, or an error otherwise."""

    @abstractmethod
    async def start(self) -> None:
        """Starts syncing proxy with proxied data source."""

    @abstractmethod
    async def stop(self) -> None:
        """Stops syncing proxy with proxied data source."""


class LPSyncProxyFromAsyncProxy(LPSyncProxy):
    """Generic adaptor to provide a LPSyncProxy from a LPAsyncProxy.

    Default implementation that simply queries and caches underlying LPSyncProxy at
    every block.
    """

    CACHE_SIZE = 25

    def __init__(
        self,
        underlying_lp_async_proxy: LPAsyncProxy,
        block_stream: BlockStream
    ):
        self.recent_state_cache = RecentStateCache(self.CACHE_SIZE)
        self.underlying_lp_async_proxy = underlying_lp_async_proxy
        self.block_stream = block_stream
        self.block_stream.subscribe(self.query_underlying_lp_async_proxy)

    async def query_underlying_lp_async_proxy(
        self,
        block_number: int,
        block_hash: str
    ):
        # Try hard to keep it in sync.
        while True:
            try:
                state = await self.underlying_lp_async_proxy(
                    block_number=block_number,
                    block_hash=block_hash
                )
                break
            except RuntimeError as err:
                logger.warning(
                    f'Could not obtain state for block {block_number} from '
                    f'underlying lp async proxy {err}. Retrying in 5 seconds ...'
                )
                await asyncio.sleep(5)

        self.recent_state_cache.add(block_number, block_hash, state)

    def __call__(self, block_number: int = None, block_hash: str = None) -> Dict[str, LP]:
        """Returns the required state if cached, or raise a CacheMissError otherwise."""
        return self.recent_state_cache.get_at_block(block_number, block_hash)

    async def start(self) -> None:
        pass
    async def stop(self) -> None:
        pass


class LPFromInitialStatePlusChangesProxy(LPSyncProxy):
    # if ethereum finality is 6 blocks,
    # we would only need to keep 6 blocks since checkpoint.
    MAX_NR_BLOCKS_TO_CHECKPOINT = 25

    def __init__(self, lp_ids, events, async_proxy, event_stream, web3_client):
        self.lp_ids = lp_ids
        self.events = events
        self.async_proxy = async_proxy
        self.web3_client = web3_client
        self.event_log = RecentEventLog(web3_client, event_stream)
        self.checkpoint = None

    async def start(self) -> None:
        logger.debug(f"Starting {self} ...")

        # since async_proxy might not be up to date,
        # it is what defines the start block.
        latest_block = await self.async_proxy.latest_block()
        start_block_number = latest_block.number - self.MAX_NR_BLOCKS_TO_CHECKPOINT
        start_block_hash = self.web3_client.eth.get_block(start_block_number).hash.hex()
        self.checkpoint = await self.async_proxy(start_block_number, start_block_hash)

        self.event_log.start(
            self.lp_ids,
            self.events,
            start_block_number,
            start_block_hash
        )

        logger.debug(f"Starting {self} ... done")

    def stop(self) -> None:
        logger.debug(f"Stopping {self} ...")
        self.event_log.stop()
        logger.debug(f"Stopping {self} ... done")

    def __call__(self, block_number: int = None, block_hash: str = None) -> Dict[str, LP]:
        """Returns a list of lps with state at (the end of) given block.

        If block hash is specified, then return lps state at that block if possible,
        otherwise will raise a CacheMissError.

        If block number is specified, then return lps state at that block if possible, 
        otherwise will raise a CacheMissError.
        """

        logger.debug(f"Querying {self} (block={block_number}) ...")
            
        state = self.get_state(self.checkpoint, self.event_log(block_number=block_number, block_hash=block_hash))

        # Update checkpoint to computed state to save extra computation and memory on
        # future calls.
        if self.event_log.block_count > self.MAX_NR_BLOCKS_TO_CHECKPOINT:
            logger.debug("Updating checkpoint.")
            nr_blocks_to_free = self.event_log.block_count - self.MAX_NR_BLOCKS_TO_CHECKPOINT
            min_start_block_number = self.event_log.start_block_number + nr_blocks_to_free
            self.checkpoint = self.get_state(self.checkpoint, self.event_log(block_number=min_start_block_number - 1))
            self.event_log.update_start_block(min_start_block_number)
            #self.checkpoint_block_hash = self.event_log.start_block_hash

        return state

    @abstractmethod
    def get_state(self, checkpoint, delta) -> Dict[str, LP]:
        """Assembles state from checkpoint and delta."""


class LPDriver(ABC):
    class LPSyncProxyDataSource(Enum):
        TheGraph = 1
        Web3 = 2
        TheGraphAndWeb3 = 3

    @abstractmethod
    def type(self) -> str:
        """Returns unique identifier for type of lp."""

    @abstractmethod
    def create_lp_sync_proxy(self, lp_ids: List[str]) -> LPSyncProxy:
        """Creates a new LPSyncProxy instance that tracks a set of lps."""

    @abstractmethod
    async def get_lp_ids(self, token_ids: List[str]) -> List[str]:
        """Collects addresses of lps involving given tokens."""

