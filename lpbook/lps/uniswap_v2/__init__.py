
import asyncio
import logging
from dataclasses import dataclass
from decimal import MAX_EMAX, MAX_PREC, MIN_EMIN, Context
from decimal import Decimal as D
from decimal import setcontext
from functools import cache
from pathlib import Path
from typing import Dict, List, Tuple

import aiohttp
from lpbook import (LPAsyncProxy, LPDriver, LPSyncProxy,
                    LPSyncProxyFromAsyncProxy)
from lpbook.error import TemporaryError
from lpbook.lps.uniswap_v2.subgraph import UniV2GraphQLClient
from lpbook.util import LP, Token
from lpbook.web3 import BlockId
from lpbook.web3.block_stream import BlockStream
from web3.exceptions import BlockNotFound, ContractLogicError

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

        with open(Path(__file__).parent / 'artifacts' / 'erc20.abi', 'r') as f:
            self.erc20_contract_abi = f.read()

    async def latest_block(self) -> BlockId:
        block = await self.client.eth.get_block()
        return BlockId(number=block.number, hash=block.hash.hex())

    @cache
    def get_tokens(self, lp_id) -> Tuple[Token, Token]:
        token0_address = self.contracts[lp_id].functions.token0().call().lower()
        token1_address = self.contracts[lp_id].functions.token1().call().lower()

        r = []
        for token_address in [token0_address, token1_address]:
            address_chksum = self.client.toChecksumAddress(token_address)
            token_contract = self.client.eth.contract(
                address=address_chksum,
                abi=self.erc20_contract_abi
            )
            decimals = token_contract.functions.decimals().call()
            symbol = token_contract.functions.symbol().call()
            r.append(Token(token_address, symbol, decimals))

        return r

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
                decimals=thegraph_data.token0.decimals
            ),
            Token(
                address=thegraph_data.token1.id,
                symbol=thegraph_data.token1.symbol,
                decimals=thegraph_data.token1.decimals
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


class UniV2Driver(LPDriver):
    def __init__(
        self,
        block_stream: BlockStream,
        session: aiohttp.ClientSession,
        web3_client=None
    ):
        super().__init__(UniV2)
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
            LPDriver.LPSyncProxyDataSource.Web3
        ]:
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

    async def get_lp_ids(self, token_ids: List[str]) -> List[str]:
        return [
            state.id async for state in self.graphql_client.get_pairs_state(
                {'token0_in': token_ids, 'token1_in': token_ids},
                field_setter=self.graphql_client.set_pair_id_field
            )
        ]