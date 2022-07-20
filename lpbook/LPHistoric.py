import logging
from typing import List

from lpbook.util import LP
from lpbook.web3 import BlockId

logger = logging.getLogger(__name__)


class LPHistoric:
    def __init__(self, lp_drivers):
        self.lp_drivers = lp_drivers

    async def get_lps_trading_tokens(self, token_ids: set, block_number) -> List[LP]:
        """Return all LPs that trade at least two tokens in token_ids at given block number.
        """

        all_lps = []
        for driver in self.lp_drivers:
            lp_ids = await driver.get_lp_ids(token_ids)
            lp_async_proxy = driver.create_lp_async_proxy(lp_ids)
            all_lps += list((await lp_async_proxy(BlockId(number=block_number))).values())

        return all_lps
