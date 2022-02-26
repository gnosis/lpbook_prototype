
import asyncio
from lib2to3.pgen2 import driver
import aiohttp
from dotenv import load_dotenv
from lpbook import LPDriver
#import pytest_asyncio
from lpbook.LPCache import LPCache
from lpbook.lps.curve import CurveDriver, CurveTheGraphAsyncProxy, CurveWeb3AsyncProxy
from lpbook.lps.uniswap_v3 import UniV3Driver, UniV3TheGraphProxy
from lpbook.lps.uniswap_v3.subgraph import UniV3GraphQLClient
from lpbook.util import LP
from lpbook.web3.block_stream import BlockStream

import os
from web3 import Web3
import logging.config

from lpbook.web3.event_stream import ServerFilteredEventStream

logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=True)

logger = logging.getLogger(__name__)

load_dotenv() 
INFURA_ID = os.getenv("INFURA_ID")


async def assert_equivalent_proxies(web3_client, proxy1, proxy2, block_stream, block_lag=0):
    """Tests if two different proxies yield exactly the same results."""

    async def check_at_block(block_number, block_hash):
        assert block_number is not None
        logger.debug(f"Asserting equivalent state at block {block_number} ...")
        lps1 = proxy1(block_hash=block_hash)
        lps2 = proxy2(block_hash=block_hash)
        lps1 = {lp_id: lps1[lp_id] for lp_id in sorted(lps1.keys())}
        lps2 = {lp_id: lps2[lp_id] for lp_id in sorted(lps2.keys())}
        if lps1 != lps2:
            for lp1, lp2 in zip(lps1.values(), lps2.values()):
                if lp1 != lp2:
                    print("different elements:")
                    print("lp1:", lp1)
                    print("lp2:" , lp2)
            if len(lps1) != len(lps2):
                print("only 1:", set(lps1)-set(lps2))
                print("only 2:", set(lps2)-set(lps1))
            assert(False)

    cur_block = web3_client.eth.get_block('latest')
    logger.debug(f"Latest block is {cur_block.number}")

    logger.debug("Starting proxies ...")
    await proxy1.start()
    await proxy2.start()
    logger.debug("Starting proxies ... done")

    logger.debug(f"Starting block index at block {cur_block.number - block_lag} ...")
    asyncio.ensure_future(block_stream.run(cur_block.number - block_lag))
    logger.debug("Starting block index ... done")

    # wait until all caches are filled
    logger.debug("Warm up cache ...")
    while block_stream.last_block_number is None or block_stream.last_block_number < cur_block.number:
        await asyncio.sleep(5)
    logger.debug("Warm up cache ... done")
    
    logger.info("Starting run loop ...")
    while True:
        cur_block_number = block_stream.last_block_number - block_lag
        if block_lag == 0:
            cur_block_hash = block_stream.last_block_hash
        else:
            cur_block = web3_client.eth.get_block(cur_block_number)
            cur_block_hash = cur_block.hash.hex()
        try:
            await check_at_block(cur_block_number, cur_block_hash)
        except RuntimeError as err:
            logger.warning(
                f"Could not sync both sources at block {cur_block_number}: {err} "
                "Retrying in 10 secs, possibly skipping block ..."
            )

        await asyncio.sleep(10)


WS_WEB3_URL = f'wss://mainnet.infura.io/ws/v3/{INFURA_ID}'
#WS_WEB3_URL = 'wss://eth-mainnet.alchemyapi.io/v2/270Ng0vUmrsinDLbgeNAldwNmuO8aDC4'
HTTP_WEB3_URL = f'https://mainnet.infura.io/v3/{INFURA_ID}'


async def test_uniswap_v3():

    token_ids = {"0x6b175474e89094c44da98b954eedeac495271d0f", "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"}

    #w3 = Web3(Web3.WebsocketProvider(WS_WEB3_URL))
    #w3 = Web3(Web3.HTTPProvider(HTTP_WEB3_URL))
    w3 = Web3(Web3.HTTPProvider('https://eth-mainnet.alchemyapi.io/v2/270Ng0vUmrsinDLbgeNAldwNmuO8aDC4'))

    block_stream = BlockStream(WS_WEB3_URL)
    event_stream = ServerFilteredEventStream(block_stream, w3)
    async with aiohttp.ClientSession() as session:
        driver_thegraph = UniV3Driver(event_stream, block_stream, session, w3)
        driver_web3 = UniV3Driver(event_stream, block_stream, session, w3)

        lp_ids = await driver_thegraph.get_lp_ids(token_ids)
        proxy_thegraph = driver_thegraph.create_lp_sync_proxy(
            lp_ids,
            LPDriver.LPSyncProxyDataSource.TheGraph
        )
        proxy_web3 = driver_web3.create_lp_sync_proxy(
            lp_ids,
            LPDriver.LPSyncProxyDataSource.TheGraphAndWeb3
        )

        await assert_equivalent_proxies(w3, proxy_thegraph, proxy_web3, block_stream, 10)


# This is currently not working, since the curve subgraph apparently is not handling
# the ramp of the amplification coefficient correctly. So if this change is currently in
# progress for some AMM, then the tests will give false failures.
# (here we're using TheGraph as the oracle)
# https://github.com/curvefi/curve-subgraph/issues/11.
async def test_curve():
    token_ids = {"0x6b175474e89094c44da98b954eedeac495271d0f", "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48".lower()}

    #w3 = Web3(Web3.WebsocketProvider(WS_WEB3_URL))
    w3 = Web3(Web3.HTTPProvider(HTTP_WEB3_URL))

    block_stream = BlockStream(WS_WEB3_URL)
    async with aiohttp.ClientSession() as session:
        driver_thegraph = CurveDriver(block_stream, session, w3, proxy=CurveDriver.Proxy.TheGraph)
        driver_web3 = CurveDriver(block_stream, session, w3, proxy=CurveDriver.Proxy.Web3)

        proxy_thegraph = driver_thegraph.create_lp_sync_proxy(await driver_thegraph.get_lp_ids(token_ids))
        proxy_web3 = driver_web3.create_lp_sync_proxy(await driver_web3.get_lp_ids(token_ids))


        await assert_equivalent_proxies(w3, proxy_thegraph, proxy_web3, block_stream, 10)

def debug():
    #w3 = Web3(Web3.HTTPProvider(HTTP_WEB3_URL))
    w3 = Web3(Web3.HTTPProvider('https://eth-mainnet.alchemyapi.io/v2/270Ng0vUmrsinDLbgeNAldwNmuO8aDC4'))

    filter_parameters = {
        "address": w3.toChecksumAddress("0xc2e9f25be6257c210d7adf0d4cd6e3e881ba25f8"),
        "fromBlock": 14269733,
        "toBlock": 14269748
    }
    filter = w3.eth.filter(filter_parameters) 
    print(filter.get_all_entries())

asyncio.run(test_uniswap_v3())
#asyncio.run(test_curve())

#async def test():
#    w3 = Web3(Web3.HTTPProvider(HTTP_WEB3_URL))
#    proxy = CurveWeb3AsyncProxy(['0xbebc44782c7db0a1a60cb6fe97d0b483032ff1c7'], w3)
#    print(await proxy(14263590))
    
#asyncio.run(test())

#debug()