import asyncio
import logging
import os
import sys
import traceback
from typing import List

import aiohttp
import uvicorn
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, Request
from lpbook.LPCache import LPCache
from lpbook.LPHistoric import LPHistoric
from lpbook.lps.curve import CurveDriver
from lpbook.lps.uniswap_v3 import UniV3Driver
from lpbook.lps.uniswap_v2 import SushiDriver, UniV2Driver
from lpbook.web3.block_stream import BlockStream
from lpbook.web3.event_stream import ServerFilteredEventStream
from pydantic import BaseSettings
from web3 import Web3

logger = logging.getLogger(__name__)

aiohttp_session = None
lp_cache = None
lp_historic = None

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
        logger.error(
            f"Unhandled exception: {str(e)}. Traceback:\n{traceback.format_exc()}\n")
        return []


@app.post("/lps_trading_tokens_historic")
async def lps_trading_tokens_historic(token_ids: List[str], block_number: int):
    """Return LPs that trade at least two tokens in the given token list at given block."""
    try:
        return [
            lp.marshall()
            for lp in await lp_historic.get_lps_trading_tokens(
                {
                    token_id.lower()
                    for token_id in token_ids
                },
                block_number=block_number
            )
        ]
    except Exception as e:
        logger.error(
            f"Unhandled exception: {str(e)}. Traceback:\n{traceback.format_exc()}\n")
        return []


@app.on_event('startup')
async def on_startup():
    global aiohttp_session
    global lp_cache
    global lp_historic

    HTTP_WEB3_URL = os.getenv('HTTP_WEB3_URL')
    WS_WEB3_URL = os.getenv('WS_WEB3_URL')

    # Components common to all drivers.
    import requests
    requests_adapter = requests.adapters.HTTPAdapter(pool_connections=20, pool_maxsize=20)
    requests_session = requests.Session()
    requests_session.mount('http://', requests_adapter)
    requests_session.mount('https://', requests_adapter)
    w3 = Web3(Web3.HTTPProvider(HTTP_WEB3_URL, session=requests_session))

    block_stream = BlockStream(WS_WEB3_URL)
    event_stream = ServerFilteredEventStream(block_stream, w3)
    aiohttp_session = aiohttp.ClientSession()

    # LP drivers
    univ3_driver = UniV3Driver(event_stream, block_stream, aiohttp_session, w3)
    curve_driver = CurveDriver(block_stream, aiohttp_session, w3)
    univ2_driver = UniV2Driver(event_stream, block_stream, aiohttp_session, w3)
    sushi_driver = SushiDriver(event_stream, block_stream, aiohttp_session, w3)

    # Create LP Cache (main service)
    # Returns current state (fast).
    #lp_cache = LPCache([univ2_driver, sushi_driver, univ3_driver, curve_driver])
    lp_cache = LPCache([univ3_driver])

    # Create LP Historic (main service)
    # Returns past state (slow).
    lp_historic = LPHistoric([univ3_driver, univ2_driver, sushi_driver])

    asyncio.ensure_future(block_stream.run())
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
