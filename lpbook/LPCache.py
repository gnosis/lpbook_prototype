import asyncio
import datetime
import logging
import traceback
from typing import List
from lpbook import LPDriver
from lpbook.error import CacheMissError

from lpbook.util import LP, traced
from lpbook.web3 import BlockId

logger = logging.getLogger(__name__)


class LPCache:
    POOL_MAX_UNUSED_AGE = datetime.timedelta(days=30)
    POOL_MAX_CACHED_AGE = datetime.timedelta(days=1)
    POOL_MIN_CACHED_AGE = datetime.timedelta(seconds=1)

    def __init__(self, lp_drivers):
        self.lp_drivers = lp_drivers
        self.cached_tokens = set()
        self.token_last_request_datetime = {}
        self.last_refresh_datetime = None
        self.lp_sync_proxies = {}
        self.lp_sync_pool_ids = {}

    def get_lps_trading_tokens(self, token_ids: set, block_number=None) -> List[LP]:
        """Return all LPs that trade at least two tokens in token_ids.

        If block is given, then the lp's state will reflect that block if that block is
        in cache, otherwise it will raise a CacheMissError.
        """
        now = datetime.datetime.now()
        for t in token_ids:
            self.token_last_request_datetime[t] = now

        # Always return immediately whatever is cached.
        all_lps = []
        for lp_sync_proxy in self.lp_sync_proxies.values():
            try:
                lps = list(lp_sync_proxy(BlockId(number=block_number)).values())
            except CacheMissError:
                logger.debug(f'LPProxy {lp_sync_proxy} still initializing. Skipping ...')
                continue
            for lp in lps:
                lp_token_ids = {t.address for t in lp.tokens}
                if len(lp_token_ids & token_ids) >= 2:
                    all_lps.append(lp)

        if len(all_lps) == 0:
            logger.warning(f'Cache miss for token_ids {token_ids}.')

        return all_lps

    @traced(logger, 'Running LP cache')
    async def run(self):
        while True:
            now = datetime.datetime.now()
            most_requested_tokens = {
                t
                for t, dt in self.token_last_request_datetime.items()
                if now - dt <= self.POOL_MAX_UNUSED_AGE
            }

            # Refresh if a) cache doesn't equal most requested tokens or
            # b) if last cache refresh was too long ago.
            # Condition a) handles cache misses and makes sure it is not
            # tracking unused tokens. Condition b) is required since new
            # lps may have been created/deleted for the recently cached
            # tokens since last refresh.
            if (
                len(most_requested_tokens) > 0 and
                self.cached_tokens != most_requested_tokens
            ) or self.last_refresh_datetime is None or \
                    now - self.last_refresh_datetime > self.POOL_MAX_CACHED_AGE:
                await self.refresh(most_requested_tokens)

            await asyncio.sleep(self.POOL_MIN_CACHED_AGE.total_seconds())

    async def refresh_driver(self, driver, tokens):
        cur_lp_sync_proxy = self.lp_sync_proxies.get(driver.protocol, None)
        cur_lp_ids = self.lp_sync_pool_ids.get(driver.protocol, set())

        try:
            new_lp_ids = set(await driver.get_lp_ids(tokens))
        except Exception as err:
            logger.error(
                f"Error querying lps for {driver.protocol}: {err}. "
                f"Traceback:\n{traceback.format_exc()}"
            )
            # Keep current proxy in case of error
            return (cur_lp_sync_proxy, cur_lp_ids)

        if len(new_lp_ids) == 0:
            class NoOpSyncProxy:
                def __call__(self, _):
                    return {}

                def stop(self):
                    pass

            return (NoOpSyncProxy(), set())

        # optimization: no need to reset proxies that return
        # the same set of pools as last time.
        if new_lp_ids == cur_lp_ids:
            return (cur_lp_sync_proxy, cur_lp_ids)

        new_lp_sync_proxy = driver.create_lp_sync_proxy(
            new_lp_ids,
            LPDriver.LPSyncProxyDataSource.Default
        )

        try:
            await new_lp_sync_proxy.start()
        except Exception as err:
            logger.error(
                f"Error starting lp sync proxy for {driver.protocol}: {err}. "
                f"Traceback:\n{traceback.format_exc()}"
            )
            return (cur_lp_sync_proxy, cur_lp_ids)

        return (new_lp_sync_proxy, new_lp_ids)

    @traced(logger, 'Refreshing LP cache')
    async def refresh(self, tokens):
        logger.debug(f'Refreshing LP cache for {len(tokens)} tokens ...')
        now = datetime.datetime.now()

        new_lp_sync_proxies = {}
        new_lp_sync_pool_ids = {}

        async def update_new(driver):
            (driver_proxy, driver_lp_ids) = \
                await self.refresh_driver(driver, tokens)
            if driver_proxy is not None:
                new_lp_sync_proxies[driver.protocol] = driver_proxy
                new_lp_sync_pool_ids[driver.protocol] = driver_lp_ids

        if len(tokens) > 0:
            await asyncio.gather(*[update_new(driver) for driver in self.lp_drivers])

        # Stop all current proxies that we won't keep
        for sync_proxy in self.lp_sync_proxies.values():
            if sync_proxy not in new_lp_sync_proxies.values():
                sync_proxy.stop()

        # Replace old with new proxies.
        self.lp_sync_proxies = new_lp_sync_proxies
        self.lp_sync_pool_ids = new_lp_sync_pool_ids
        self.cached_tokens = tokens
        self.last_refresh_datetime = now
