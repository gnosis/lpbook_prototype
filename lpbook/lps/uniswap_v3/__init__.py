from enum import Enum
import logging
from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List

import aiohttp
from lpbook import (LPSyncProxyFromAsyncProxy, LPSyncProxy, LPAsyncProxy, LPDriver,
                          LPFromInitialStatePlusChangesProxy)
from lpbook.util import LP, Token
from lpbook.web3 import Block
from lpbook.web3.RecentEventLog import RecentEventLog
from lpbook.web3.BlockIndex import BlockIndex

from .subgraph import UniV3GraphQLClient

logger = logging.getLogger(__name__)


@dataclass
class UniV3(LP):
    """Represents a UniswapV3 LP."""
    address: str
    token0: Token
    token1: Token
    sqrt_price: int
    liquidity: int
    tick: int    
    liquidity_net: Dict[int, int]

    @property
    def uid(self) -> str:
        return self.address

    @property
    def type(self) -> str:
        return 'UniswapV3'

    @property
    def tokens(self) -> List[Token]:
        return [self.token0, self.token1]

    @property
    def state(self) -> Dict:
        return {
            "sqrt_price": self.sqrt_price,
            "liquidiy": self.liquidity,
            "tick": self.tick,
            "liquidity_net": self.liquidity_net
        }


class UniV3TheGraphProxy(LPAsyncProxy):
    """"Loads the state of liquidity from TheGraph."""
    def __init__(self, lp_ids, uniswap_v3_gql_client):
        assert len(lp_ids) >= 1
        self.lp_ids = lp_ids
        self.client = uniswap_v3_gql_client

    def create_from_thegraph(self, thegraph_data) -> UniV3:
        return UniV3(
            address=thegraph_data.id,
            token0=Token(
                address=thegraph_data.token0.id,
                symbol=thegraph_data.token0.symbol,
                decimals=int(thegraph_data.token0.decimals)
            ),
            token1=Token(
                address=thegraph_data.token1.id,
                symbol=thegraph_data.token1.symbol,
                decimals=int(thegraph_data.token1.decimals)
            ),
            sqrt_price=int(thegraph_data.sqrt_price),
            liquidity=int(thegraph_data.liquidity),
            tick=int(thegraph_data.tick),
            liquidity_net={int(tick.tick_idx): int(tick.liquidity_net) for tick in thegraph_data.ticks}
        )

    async def latest_block(self) -> Block:
        block = await self.client.get_last_block()
        return Block(number=block.number, hash=str(block.hash))

    async def __call__(self, block_number: int = None, block_hash: str = None) -> Dict[str, LP]:
        shortened_block_hash = block_hash[:8] if block_hash is not None else None
        logger.debug(f"Retrieving uniswap V3 state from TheGraph at block {block_number}/{shortened_block_hash} ...")

        block = {}
        if block_hash is not None:
            block.update(hash=block_hash)
        elif block_number is not None:
            block.update(number=block_number)
        extra_kwargs = {}
        if len(block) > 0:
            extra_kwargs = {"block": block}

        # this is to workaround a current thegraph bug (already reported and confirmed),
        # where thegraph replies with arbitrary data when the passed block number/hash is
        # not yet indexed.
        if block_number is not None:
            latest_block_number = (await self.latest_block()).number
            if block_number > latest_block_number:
                logger.debug(f"{self} is lagging behind {block_number - latest_block_number} blocks.")
                raise RuntimeError(f"Attempt to retrieve a block too recent for {self}")

        # Perform a more efficient query if we're tracking a single LP.
        if len(self.lp_ids) == 1:
            lp_id = self.lp_ids[0]
            thegraph_lp_data = await self.client.get_pool_state_and_ticks(lp_id, **extra_kwargs)
            state = {lp_id: self.create_from_thegraph(thegraph_lp_data)}
        else:
            lp_filter = {"id_in": self.lp_ids}
            thegraph_data = await self.client.get_pools_state_and_ticks(lp_filter, {}, **extra_kwargs)
            state = {thegraph_lp_data.id: self.create_from_thegraph(thegraph_lp_data) for thegraph_lp_data in thegraph_data}

        #logger.debug(state)
        return state


class UniV3EventLog(RecentEventLog):
    def __init__(self, lp_ids, web3_client, block_index):

        # read abi from same directory as this file.
        with open(Path(__file__).parent / "artifacts" / "uniswap_v3.abi", "r") as f:
            contract_abi = f.read()
        UniV3 = web3_client.eth.contract(abi=contract_abi)

        super().__init__(
            lp_ids,
            [UniV3.events.Swap, UniV3.events.Burn, UniV3.events.Mint],
            web3_client,
            block_index
        )


class UniV3TheGraphAndWeb3Proxy(LPFromInitialStatePlusChangesProxy):
    """Queries TheGraph for an initial state, and web3 for state updates."""

    def get_state(self, prev_state: Dict[str, LP], changes: List[Any]) -> Dict[str, LP]:
        """Assembles state from checkpoint and changes."""

        cur_state = deepcopy(prev_state) 

        for d in changes:
            lp_id = d.address.lower()
            assert lp_id in cur_state.keys()
            lp_cur_state = cur_state[lp_id]

            if d.event == 'Swap':
                lp_cur_state.tick = d.args.tick
                lp_cur_state.liquidity = d.args.liquidity
                lp_cur_state.sqrt_price = d.args.sqrtPriceX96

            elif d.event == 'Mint':
                tick_lower = d.args.tickLower
                tick_upper = d.args.tickUpper

                # liquidity tracks the liquidity on recent tick,
                # only need to update it if the new position includes the recent tick.
                if lp_cur_state.tick <= tick_lower and lp_cur_state.tick > tick_upper:
                    lp_cur_state.liquidity += d.args.amount
                
                if tick_lower not in lp_cur_state.liquidity_net.keys():
                    lp_cur_state.liquidity_net[tick_lower] = 0

                if tick_upper not in lp_cur_state.liquidity_net.keys():
                    lp_cur_state.liquidity_net[tick_upper] = 0

                lp_cur_state.liquidity_net[tick_lower] += d.args.amount
                lp_cur_state.liquidity_net[tick_upper] -= d.args.amount

            elif d.event == 'Burn':
                tick_lower = d.args.tickLower
                tick_upper = d.args.tickUpper

                # liquidity tracks the liquidity on recent tick,
                # only need to update it if the new position includes the recent tick.
                if lp_cur_state.tick <= tick_lower and lp_cur_state.tick > tick_upper:
                    lp_cur_state.liquidity -= d.args.amount

                if tick_lower not in lp_cur_state.liquidity_net.keys():
                    lp_cur_state.liquidity_net[tick_lower] = 0

                if tick_upper not in lp_cur_state.liquidity_net.keys():
                    lp_cur_state.liquidity_net[tick_upper] = 0

                lp_cur_state.liquidity_net[tick_lower] -= d.args.amount
                lp_cur_state.liquidity_net[tick_upper] += d.args.amount

            else:
                assert False

        return cur_state


class UniV3Driver(LPDriver):
    class Proxy(Enum):
        TheGraph = 1
        TheGraphAndWeb3 = 2

    def __init__(self, block_index: BlockIndex, session: aiohttp.ClientSession, web3_client, proxy : Proxy=Proxy.TheGraphAndWeb3):
        self.block_index = block_index
        self.web3_client = web3_client
        self.graphql_client = UniV3GraphQLClient(session)
        self.proxy = proxy

    def type(self) -> str:
        return "UniswapV3"

    def create_lp_sync_proxy(self, lp_ids: List[str]) -> LPSyncProxy:
        async_proxy = UniV3TheGraphProxy(lp_ids, self.graphql_client)
        if self.proxy == UniV3Driver.Proxy.TheGraphAndWeb3:
            event_log = UniV3EventLog(lp_ids, self.web3_client, self.block_index)
            sync_proxy = UniV3TheGraphAndWeb3Proxy(async_proxy, event_log)
        else:
            sync_proxy = LPSyncProxyFromAsyncProxy(async_proxy, self.block_index)
        return sync_proxy

    async def get_lp_ids(self, token_ids: List[str]) -> List[str]:
        return [
            state.id async for state in self.graphql_client.get_pools_state(
            {'token0_in': token_ids, 'token1_in': token_ids},
            field_setter=self.graphql_client.set_pool_id_field
        )]
