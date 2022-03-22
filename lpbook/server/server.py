import asyncio
import logging
import os
from typing import List

import aiohttp
import uvicorn
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, Request
from lpbook.LPCache import LPCache
from lpbook.cost.gas_stats_collector import GasStatsCollector
from lpbook.lps.curve import CurveDriver
from lpbook.lps.uniswap_v3 import UniV3Driver
from lpbook.web3.block_stream import BlockStream
from lpbook.web3.event_stream import ServerFilteredEventStream
from pydantic import BaseSettings
from web3 import Web3

logger = logging.getLogger(__name__)

aiohttp_session = None
lp_cache = None
gas_statistics = None

# ++++ Interface definition ++++


# Server settings: Can be overriden by passing them as env vars or in a .env file.
# Example: PORT=8001 python -m src._server
class ServerSettings(BaseSettings):
    host: str = '127.0.0.1'
    port: int = 8000

    class Config:
        env_file = '.env'


server_settings = ServerSettings()


app = FastAPI(
    title="LPBook service"
)


@app.get("/health", status_code=200)
def health():
    """Convenience endpoint to check if server is alive."""
    return True


@app.post("/lps_trading_tokens")
async def lps_trading_tokens(token_ids: List[str]):
    """Return LPs that trade at least two tokens in the given token list."""
    try:
        return [
            lp.marshall()
            for lp in lp_cache.get_lps_trading_tokens({
                token_id.lower()
                for token_id in token_ids
            })
        ]
    except Exception as e:
        logger.error(f"Unhandled exception: {str(e)}.")
        return []


@app.on_event('startup')
async def on_startup():
    global aiohttp_session
    global lp_cache

    HTTP_WEB3_URL = os.getenv('HTTP_WEB3_URL')
    WS_WEB3_URL = os.getenv('WS_WEB3_URL')

    # Components common to all drivers.
    w3 = Web3(Web3.HTTPProvider(HTTP_WEB3_URL))
    block_stream = BlockStream(WS_WEB3_URL)
    event_stream = ServerFilteredEventStream(block_stream, w3)
    aiohttp_session = aiohttp.ClientSession()

    gas_stats_collector = GasStatsCollector()
    await gas_stats_collector.initialize()

    # LP drivers
    univ3_driver = UniV3Driver(event_stream, block_stream, aiohttp_session, w3)
    curve_driver = CurveDriver(block_stream, aiohttp_session, w3)

    # Create LP Cache (main service)
    lp_cache = LPCache([univ3_driver, curve_driver], gas_stats_collector)

    asyncio.ensure_future(block_stream.run())
    asyncio.ensure_future(gas_stats_collector.run())
    asyncio.ensure_future(lp_cache.run())


@app.on_event('shutdown')
async def on_shutdown():
    await aiohttp_session.close()

# ++++ Server setup: ++++


if __name__ == '__main__':
    # Load local environment variables from .env file.
    load_dotenv()

    logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=True)

    load_dotenv()

    uvicorn.run(
        "__main__:app",
        host=server_settings.host,
        port=server_settings.port,
        log_level="warning",
        loop='asyncio'
    )
