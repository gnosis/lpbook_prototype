
import asyncio
from copy import deepcopy
import logging
from dataclasses import dataclass
from decimal import MAX_EMAX, MAX_PREC, MIN_EMIN, Context
from decimal import Decimal as D
from decimal import setcontext
from functools import cache
from pathlib import Path
from typing import Any, Dict, List, Tuple

import aiohttp
from lpbook import (LPAsyncProxy, LPDriver, LPFromInitialStatePlusChangesProxy, LPSyncProxy,
                    LPSyncProxyFromAsyncProxy)
from lpbook.error import TemporaryError
from lpbook.lps.uniswap_v2.subgraph import UniV2GraphQLClient
from lpbook.util import LP, Token
from lpbook.web3 import BlockId, create_token_from_web3
from lpbook.web3.block_stream import BlockStream
from web3.exceptions import BlockNotFound, ContractLogicError

from lpbook.web3.event_stream import EventStream

setcontext(Context(prec=MAX_PREC, Emax=MAX_EMAX, Emin=MIN_EMIN))

logger = logging.getLogger(__name__)


@dataclass
class UniV2(LP):
    """Uniswap V2 LP."""
    address: str
    _tokens: List[Token]
    balances: List[int]

    @property
    def tokens(self) -> List[Token]:
        return self._tokens

    @property
    def uid(self) -> str:
        return self.address

    @classmethod
    @property
    def protocol_name(self) -> str:
        return 'Uniswap'

    @classmethod
    @property
    def protocol_version(self) -> str:
        return '2'

    @property
    def state(self) -> Dict:
        return {
            'balances': self.balances
        }

    @classmethod
    @property
    def gas_stats(self) -> Dict:
        # See https://dune.com/queries/1043253 .
        return {
            'nr_obs': 39409,
            'mean': 112091.89634347484,
            'stddev': 42717.69677854,
            'min': 30132,
            'max': 695127,
            'median': 97511
        }


class UniV2Web3AsyncProxy(LPAsyncProxy):
    """"Proxies the state of the uniswap v2 LP through web3."""

    def __init__(self, lp_ids, web3_client):
        assert len(lp_ids) >= 1
        self.lp_ids = lp_ids
        self.client = web3_client
        self.contracts = {}

        with open(Path(__file__).parent / 'artifacts' / 'uniswap_v2.abi', 'r') as f:
            contract_abi = f.read()
            for lp_id in lp_ids:
                lp_id_chksum = self.client.toChecksumAddress(lp_id)
                self.contracts[lp_id] = web3_client.eth.contract(
                    address=lp_id_chksum,
                    abi=contract_abi
                )

    async def latest_block(self) -> BlockId:
        block = await self.client.eth.get_block()
        return BlockId(number=block.number, hash=block.hash.hex())

    @cache
    def get_tokens(self, lp_id) -> Tuple[Token, Token]:
        token0_address = self.contracts[lp_id].functions.token0().call().lower()
        token1_address = self.contracts[lp_id].functions.token1().call().lower()

        tokens = []
        for token_address in [token0_address, token1_address]:
            address_chksum = self.client.toChecksumAddress(token_address)
            tokens.append(create_token_from_web3(address_chksum, self.client))

        return tokens

    def create_from_blockchain(self, lp_id, block: BlockId) -> UniV2:
        block_identifier = block.to_web3()

        token0, token1 = self.get_tokens(lp_id)
        balance0, balance1, _ = self.contracts[lp_id].functions.getReserves().call(
            block_identifier=block_identifier
        )
        return UniV2(
            address=lp_id,
            _tokens=[token0, token1],
            balances=[balance0, balance1],
        )

    async def __call__(
        self,
        block: BlockId
    ) -> Dict[str, LP]:

        logger.debug(
            f'Retrieving uni v2 state from blockchain at block {block} ...'
        )

        state = {}

        async def add_to_state(lp_id):
            try:
                state[lp_id] = await asyncio.to_thread(
                    self.create_from_blockchain,
                    lp_id,
                    block
                )
            except BlockNotFound as e:
                raise TemporaryError(str(e))
            except ContractLogicError as e:
                logger.error(
                    f"Transaction reverted when querying pool {lp_id}. Consider denylisting."
                )
                raise e
            except ValueError as e:
                if e.args[0]['code'] == -32000:
                    raise TemporaryError(str(e))
                raise e

        await asyncio.gather(
            *[add_to_state(lp_id) for lp_id in self.lp_ids]
        )

        # logger.debug(state)
        return state


class UniV2TheGraphAsyncProxy(LPAsyncProxy):
    """"Proxies the state of the uniswap v2 LP through TheGraph."""
    def __init__(self, lp_ids, uniswap_v2_gql_client):
        assert len(lp_ids) >= 1
        self.lp_ids = lp_ids
        self.client = uniswap_v2_gql_client

    def create_from_thegraph(self, thegraph_data) -> UniV2:
        tokens = [
            Token(
                address=thegraph_data.token0.id,
                symbol=thegraph_data.token0.symbol,
                decimals=int(thegraph_data.token0.decimals)
            ),
            Token(
                address=thegraph_data.token1.id,
                symbol=thegraph_data.token1.symbol,
                decimals=int(thegraph_data.token1.decimals)
            )
        ]
        balances = [
            D(thegraph_data.reserve0) * 10**int(tokens[0].decimals),
            D(thegraph_data.reserve1) * 10**int(tokens[1].decimals)
        ]

        return UniV2(
            address=thegraph_data.id,
            _tokens=tokens,
            balances=balances
        )

    async def latest_block(self) -> BlockId:
        block = await self.client.get_last_block()
        return BlockId(number=block.number, hash=str(block.hash))

    async def __call__(
        self,
        block: BlockId
    ) -> Dict[str, LP]:
        logger.debug(
            f'Retrieving uniswap v2 state from TheGraph at block {block} ...'
        )

        extra_kwargs = block.to_thegraph_filter()

        # this is to workaround a current thegraph bug (already reported and confirmed),
        # where thegraph replies with arbitrary data when the passed block number/hash is
        # not yet indexed.
        if block.number is not None:
            latest_block_number = (await self.latest_block()).number
            if block.number > latest_block_number:
                logger.debug(
                    f'{self} is lagging behind '
                    f'{block.number - latest_block_number} blocks.'
                )
                raise RuntimeError(f'Attempt to retrieve a block too recent for {self}')

        lp_filter = {
            'id_in': self.lp_ids,
        }
        thegraph_data = [
            pair
            async for pair in self.client.get_pairs_state(lp_filter, None, **extra_kwargs)
        ]
        state = {
            thegraph_lp_data.id: self.create_from_thegraph(thegraph_lp_data)
            for thegraph_lp_data in thegraph_data
        }

        # logger.debug(state)
        return state


class UniV2TheGraphAndWeb3Proxy(LPFromInitialStatePlusChangesProxy):
    """Queries TheGraph for an initial state, and web3 for state updates."""

    def __init__(self, lp_ids, async_proxy, event_stream, web3_client):
        # read abi from same directory as this file.
        with open(Path(__file__).parent / 'artifacts' / 'uniswap_v2.abi', 'r') as f:
            contract_abi = f.read()
        UniV2 = web3_client.eth.contract(abi=contract_abi)

        super().__init__(
            lp_ids,
            [UniV2.events.Swap, UniV2.events.Burn, UniV2.events.Mint],
            async_proxy,
            event_stream,
            web3_client
        )

    def get_state(self, prev_state: Dict[str, LP], changes: List[Any]) -> Dict[str, LP]:
        """Assembles state from previous state and updates."""

        cur_state = deepcopy(prev_state)

        for d in changes:
            lp_id = d.address.lower()
            assert lp_id in cur_state.keys()
            lp_cur_state = cur_state[lp_id]

            if d.event == 'Swap':
                lp_cur_state.balances[0] += d.args.amount0In
                lp_cur_state.balances[0] -= d.args.amount0Out
                lp_cur_state.balances[1] += d.args.amount1In
                lp_cur_state.balances[1] -= d.args.amount1Out

            elif d.event == 'Mint':
                lp_cur_state.balances[0] += d.args.amount0
                lp_cur_state.balances[1] += d.args.amount1

            elif d.event == 'Burn':
                lp_cur_state.balances[0] -= d.args.amount0
                lp_cur_state.balances[1] -= d.args.amount1

            else:
                assert False

        return cur_state


class UniV2Driver(LPDriver):
    def __init__(
        self,
        event_stream: EventStream,
        block_stream: BlockStream,
        session: aiohttp.ClientSession,
        web3_client=None
    ):
        super().__init__(UniV2)
        self.event_stream = event_stream
        self.block_stream = block_stream
        self.web3_client = web3_client
        self.graphql_client = UniV2GraphQLClient(session)

    def create_lp_sync_proxy(
        self,
        lp_ids: List[str],
        data_source: LPDriver.LPSyncProxyDataSource =
            LPDriver.LPSyncProxyDataSource.Default
    ) -> LPSyncProxy:
        if data_source in [
            LPDriver.LPSyncProxyDataSource.Default,
            LPDriver.LPSyncProxyDataSource.TheGraphAndWeb3
        ]:
            async_proxy = UniV2TheGraphAsyncProxy(
                lp_ids, self.graphql_client
            )
            return UniV2TheGraphAndWeb3Proxy(
                lp_ids,
                async_proxy,
                self.event_stream,
                self.web3_client
            )
        elif data_source == LPDriver.LPSyncProxyDataSource.Web3:
            async_proxy = UniV2Web3AsyncProxy(lp_ids, self.web3_client)
        else:
            assert data_source == LPDriver.LPSyncProxyDataSource.TheGraph
            async_proxy = UniV2TheGraphAsyncProxy(
                lp_ids, self.graphql_client
            )
        sync_proxy = LPSyncProxyFromAsyncProxy(
            async_proxy, self.block_stream
        )
        return sync_proxy

    def create_lp_async_proxy(
        self,
        lp_ids: List[str],
        data_source: LPDriver.LPAsyncProxyDataSource =
            LPDriver.LPAsyncProxyDataSource.Default
    ) -> LPAsyncProxy:
        if data_source in [
            LPDriver.LPAsyncProxyDataSource.Default,
            LPDriver.LPAsyncProxyDataSource.TheGraph
        ]:
            return UniV2TheGraphAsyncProxy(
                lp_ids, self.graphql_client
            )
        elif data_source == LPDriver.LPAsyncProxyDataSource.Web3:
            return UniV2Web3AsyncProxy(lp_ids, self.web3_client)

        raise RuntimeError("Invalid data_source for async_proxy to UniV2")

    async def get_lp_ids(self, token_ids: List[str]) -> List[str]:
        def is_valid_token(token):
            return token.symbol is not None and len(token.symbol) > 0 and \
                token.decimals is not None

        return [
            state.id
            async for state in self.graphql_client.get_pairs_state(
                {
                    'token0_in': token_ids,
                    'token1_in': token_ids,
                    'volume_usd_gt': 1000
                },
                field_setter=self.graphql_client.set_pair_id_and_tokens_fields
            )
            if is_valid_token(state.token0) and is_valid_token(state.token1)
        ]
