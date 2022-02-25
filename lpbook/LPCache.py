import asyncio
import datetime
import logging
from dataclasses import dataclass
from typing import FrozenSet, List

#from lpbook import get_lps_from_state
from lpbook.util import LP

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
        self.recent_lp_state_proxies = {}

    def get_lps_involving_tokens(self, token_ids: set, block_number=None) -> List[LP]:
        """Return all LPs involving token_ids.
        
        If block is given, then the lp's state will reflect that block if that block is in cache, otherwise
        it will raise a CacheMissError.
        """
        now = datetime.datetime.now()
        for t in token_ids:
            self.token_last_request_datetime[t] = now

        # Always return immediately whatever is cached.
        all_lps = []
        for recent_lp_state_proxy in self.recent_lp_state_proxies.values():
            lps = list(recent_lp_state_proxy(block_number=block_number).values())
            for lp in lps:
                lp_token_ids = {t.address for t in lp.tokens}
                if len(lp_token_ids & token_ids) >= 2:
                    all_lps.append(lp)

        if len(all_lps) == 0:
            logger.warning(f"Cache miss for token_ids {token_ids}.")

        return all_lps

    async def run(self):
        logger.debug("Starting lp cache ...")
        while True:
            now = datetime.datetime.now()
            most_requested_tokens = {
                t 
                for t, dt in self.token_last_request_datetime.items()
                if now - dt <= self.POOL_MAX_UNUSED_AGE
            }

            # Refresh if a) cache doesn't equal most requested tokens 
            # or b) if last cache refresh was too long ago.
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

    async def refresh(self, tokens):
        logger.debug(f"Refreshing lp cache for {len(tokens)} tokens ....")
        now = datetime.datetime.now()

        # stop all recently syncing lps
        for s in self.recent_lp_state_proxies:
            s.stop()

        self.recent_lp_state_proxies = {}
        if len(tokens) > 0:
            for d in self.lp_drivers:
                lp_ids = await d.get_lp_ids(tokens)
                if len(lp_ids) == 0:
                    continue
                recent_lp_state_proxy = d.create_lp_sync_proxy(lp_ids)
                asyncio.ensure_future(recent_lp_state_proxy.start())
                self.recent_lp_state_proxies[d.type()] = recent_lp_state_proxy

        self.cached_tokens = tokens
        self.last_refresh_datetime = now
