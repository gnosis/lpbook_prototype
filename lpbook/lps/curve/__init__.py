
import asyncio
import logging
from dataclasses import dataclass
from decimal import MAX_EMAX, MAX_PREC, MIN_EMIN, Context
from decimal import Decimal as D
from decimal import setcontext
from functools import cache
from pathlib import Path
from typing import Dict, List

import aiohttp
from lpbook import (LPAsyncProxy, LPDriver, LPSyncProxy,
                    LPSyncProxyFromAsyncProxy)
from lpbook.error import TemporaryError
from lpbook.lps.curve.subgraph import CurveGraphQLClient
from lpbook.util import LP, Token
from lpbook.web3 import BlockId, create_token_from_web3
from lpbook.web3.block_stream import BlockStream
from web3.constants import ADDRESS_ZERO
from web3.exceptions import BlockNotFound, ContractLogicError

setcontext(Context(prec=MAX_PREC, Emax=MAX_EMAX, Emin=MIN_EMIN))

logger = logging.getLogger(__name__)


@dataclass
class Curve(LP):
    """Curve LP."""
    address: str
    _tokens: List[Token]
    amplification_parameter: int
    balances: List[int]
    fee: int

    @property
    def tokens(self) -> List[Token]:
        return self._tokens

    @property
    def uid(self) -> str:
        return self.address

    @classmethod
    @property
    def protocol_name(self) -> str:
        return 'Curve'

    @classmethod
    @property
    def protocol_version(self) -> str:
        return ''

    @classmethod
    @property
    def gas_stats(self) -> Dict:
        # See https://dune.com/queries/1044860 .
        return {
            'nr_obs': 6463,
            'mean': 150158.00061890762,
            'stddev': 42372.3387235,
            'min': 64177,
            'max': 690906,
            'median': 140940
        }

    @property
    def state(self) -> Dict:
        return {
            'amplification_parameter': self.amplification_parameter,
            'fee': self.fee,
            'balances': self.balances
        }


class CurveWeb3AsyncProxy(LPAsyncProxy):
    """"Proxies the state of the curve LP through web3."""

    REGISTRY_CONTRACT_ADDRESS = '0x90e00ace148ca3b23ac1bc8c240c2a7dd9c2d7f5'

    def __init__(self, lp_ids, web3_client):
        assert len(lp_ids) >= 1
        self.lp_ids = lp_ids
        self.client = web3_client

        with open(Path(__file__).parent / 'artifacts' / 'registry.abi', 'r') as f:
            registry_contract_abi = f.read()
            registry_chksum = web3_client.toChecksumAddress(
                self.REGISTRY_CONTRACT_ADDRESS
            )
            self.registry_contract = web3_client.eth.contract(
                address=registry_chksum,
                abi=registry_contract_abi
            )

    async def latest_block(self) -> BlockId:
        block = await self.client.eth.get_block()
        return BlockId(number=block.number, hash=block.hash.hex())

    @cache
    def get_tokens(self, lp_id_chksum) -> List[Token]:
        coins = self.registry_contract.functions.get_coins(lp_id_chksum).call()
        tokens = []
        i = 0
        while coins[i] != ADDRESS_ZERO:
            tokens.append(create_token_from_web3(coins[i], self.client))
            i += 1
        return tokens

    def create_from_blockchain(self, lp_id, block: BlockId) -> Curve:
        block_identifier = block.to_web3()
        lp_id_chksum = self.client.toChecksumAddress(lp_id)

        balances = self.registry_contract.functions.get_balances(lp_id_chksum).call(
            block_identifier=block_identifier
        )
        tokens = self.get_tokens(lp_id_chksum)
        nr_tokens = len(tokens)
        balances = balances[:nr_tokens]

        parameters = self.registry_contract.functions.get_parameters(lp_id_chksum).call(
            block_identifier=block_identifier
        )

        PARAMETER_A_IDX = 0
        PARAMETER_FEE_IDX = 2
        return Curve(
            address=lp_id,
            _tokens=tokens,
            amplification_parameter=parameters[PARAMETER_A_IDX],
            balances=balances,
            fee=D(parameters[PARAMETER_FEE_IDX])/D(1e10),
        )

    async def __call__(
        self,
        block: BlockId
    ) -> Dict[str, LP]:

        logger.debug(
            f'Retrieving curve state from blockchain at block {block} ...'
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


class CurveTheGraphAsyncProxy(LPAsyncProxy):
    """"Proxies the state of the curve LP through TheGraph."""
    def __init__(self, lp_ids, curve_gql_client):
        assert len(lp_ids) >= 1
        self.lp_ids = lp_ids
        self.client = curve_gql_client

    def create_from_thegraph(self, thegraph_data) -> Curve:
        tokens = [None] * len(thegraph_data.coins)
        balances = [None] * len(thegraph_data.coins)
        for coin in thegraph_data.coins:
            tokens[coin.index] = Token(
                address=coin.token.id,
                symbol=coin.token.symbol,
                decimals=int(coin.token.decimals)
            )
            balances[coin.index] = int(D(coin.balance) * 10**int(coin.token.decimals))

        return Curve(
            address=thegraph_data.id,
            _tokens=tokens,
            amplification_parameter=int(thegraph_data.a),
            balances=balances,
            fee=D(thegraph_data.fee),
        )

    async def latest_block(self) -> BlockId:
        block = await self.client.get_last_block()
        return BlockId(number=block.number, hash=str(block.hash))

    async def __call__(
        self,
        block: BlockId
    ) -> Dict[str, LP]:
        logger.debug(
            f'Retrieving curve state from TheGraph at block {block} ...'
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
            pool
            async for pool in self.client.get_pools_state(lp_filter, None, **extra_kwargs)
        ]
        state = {
            thegraph_lp_data.id: self.create_from_thegraph(thegraph_lp_data)
            for thegraph_lp_data in thegraph_data
        }

        # logger.debug(state)
        return state


class CurveDriver(LPDriver):
    def __init__(
        self,
        block_stream: BlockStream,
        session: aiohttp.ClientSession,
        web3_client=None
    ):
        super().__init__(Curve)
        self.block_stream = block_stream
        self.web3_client = web3_client
        self.graphql_client = CurveGraphQLClient(session)

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
            async_proxy = CurveWeb3AsyncProxy(lp_ids, self.web3_client)
        else:
            assert data_source == LPDriver.LPSyncProxyDataSource.TheGraph
            async_proxy = CurveTheGraphAsyncProxy(
                lp_ids, self.graphql_client
            )
        sync_proxy = LPSyncProxyFromAsyncProxy(
            async_proxy, self.block_stream
        )
        return sync_proxy

    async def get_lp_ids(self, token_ids: List[str]) -> List[str]:
        DENYLIST = [
            # For some reason can't interact with these pools
            '0x80466c64868e1ab14a1ddf27a676c3fcbe638fe5',
            '0x4e0915c88bc70750d68c481540f081fefaf22273',
            '0x1005f7406f32a61bd760cfa14accd2737913d546'
        ]
        return {
            lp.id
            async for lp in self.graphql_client.get_pools_state(
                {
                    'is_meta': False,
                    'removed_at': None,
                    'registry_address': CurveWeb3AsyncProxy.REGISTRY_CONTRACT_ADDRESS,
                    'id_not_in': DENYLIST
                }
            )
            if len({coin.token.id for coin in lp.coins} & set(token_ids)) >= 2
        }
