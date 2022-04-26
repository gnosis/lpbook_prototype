import asyncio
import datetime
import logging.config
import os.path
from pathlib import Path
import pickle
from math import sqrt
import dateutil

from dotenv import load_dotenv
from lpbook.util import traced, traced_context
from scipy.stats import describe

from .dune_analytics import DuneAnalytics, Network


load_dotenv()

logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=True)

logger = logging.getLogger(__name__)


def get_datafile_path():
    trade_data_path = os.getenv('TRADE_DATA_PATH')
    if trade_data_path is None:
        trade_data_path = Path(__file__).parent
    else:
        trade_data_path = Path(trade_data_path)
    return trade_data_path / 'traded_data.pickled'


class GasStatsCollector:
    DATAFILE = get_datafile_path()

    def __init__(
        self,
        refresh_interval=datetime.timedelta(days=10),
        data_time_interval=datetime.timedelta(days=7)
    ):
        """Queries and assembles gas statistics from dex trades in dune analytics.

        refresh_interval: how often to query dune.
        data_time_interval: how long should the dataset span
        """
        self.refresh_interval = refresh_interval
        self.data_time_interval = data_time_interval

    @classmethod
    def get_query(cls, from_date_time, to_date_time):
        from_date_time_str = from_date_time.strftime('%Y-%m-%d %H:%M')
        to_date_time_str = to_date_time.strftime('%Y-%m-%d %H:%M')
        query = f"""
        select concat(project, '_', version) as project_and_version,
        exchange_contract_address as address,
        ethereum.transactions.gas_used,
        dex.trades.block_time as block_time
        from dex.trades
        inner join ethereum.transactions on
        dex.trades.tx_hash = ethereum.transactions.hash
        where
        dex.trades.block_time >= '{from_date_time_str}' and
        dex.trades.block_time < '{to_date_time_str}'
        """
        return query

    def load_trade_data_from_disk(self):
        with open(self.DATAFILE, 'rb') as f:
            self.data = pickle.load(f)

    def dump_trade_data_to_disk(self):
        with open(self.DATAFILE, 'wb+') as f:
            pickle.dump(self.data, f)

    @traced(logger, 'Querying dex trades from Dune Analytics')
    async def load_trade_data_from_dune(self, start_time, end_time):
        dune_connection = DuneAnalytics.new_from_environment()
        max_time_per_query = datetime.timedelta(days=7)
        data = []
        while start_time < end_time:
            next_start_time = min(end_time, start_time + max_time_per_query)
            data += await asyncio.to_thread(
                dune_connection.fetch,
                query_str=self.get_query(start_time, next_start_time),
                network=Network.MAINNET,
                parameters=[]
            )
            start_time = next_start_time
            if start_time < end_time:
                asyncio.sleep(10)
        return data

    def __call__(self, project_and_version, address):
        address = address.replace('0x', '\\x')
        if self.stats_by_address is not None and \
                address in self.stats_by_address:
            return self.stats_by_address[address]
        if self.stats_by_protocol is not None and \
                project_and_version in self.stats_by_protocol:
            return self.stats_by_protocol[project_and_version]

        logger.warning(f"No gas stats for {project_and_version} LP @ {address}")
        return None

    def compute_stats_helper(self, data):
        d = describe(data)
        quantiles = [0, 0.5, 0.95, 0.99, 1]
        sorted_data = sorted(data)
        return {
            'nr_obs': d.nobs,
            'mean': d.mean,
            'stddev': sqrt(d.variance),
            'quantiles': {
                q: sorted_data[min(len(data) - 1, int(q * len(data)))]
                for q in quantiles
            }
        }

    def cache_stats(self):
        trade_data_by_address = {}
        trade_data_by_protocol = {}
        for r in self.data:
            address, protocol, gas_used = r['address'], r['project_and_version'], r['gas_used']
            if address not in trade_data_by_address.keys():
                trade_data_by_address[address] = []
            trade_data_by_address[address].append(gas_used)

            if protocol not in trade_data_by_protocol.keys():
                trade_data_by_protocol[protocol] = []
            trade_data_by_protocol[protocol].append(gas_used)

        self.stats_by_address = {}
        for address, gas_used_sample in trade_data_by_address.items():
            if len(gas_used_sample) >= 2:
                self.stats_by_address[address] = \
                    self.compute_stats_helper(gas_used_sample)

        self.stats_by_protocol = {}
        for protocol, gas_used_sample in trade_data_by_protocol.items():
            if len(gas_used_sample) >= 2:
                self.stats_by_protocol[protocol] = \
                    self.compute_stats_helper(gas_used_sample)

    @traced(logger, 'Initializing GasStatsCollector')
    async def initialize(self):
        # Try to load from disk, and then from dune if not in disk
        try:
            self.load_trade_data_from_disk()
        except FileNotFoundError:
            while True:
                try:
                    end_time = datetime.datetime.now()
                    start_time = end_time - self.data_time_interval
                    self.data = await self.load_trade_data_from_dune(start_time, end_time)
                    self.dump_trade_data_to_disk()
                    return
                except RuntimeError as err:
                    logger.error(f"Exception loading data from dune: {err}. Retrying ...")
        self.cache_stats()

    @traced(logger, 'Running GasStatsCollector')
    async def run(self):

        while True:
            now = datetime.datetime.now()
            last_modified = datetime.datetime.fromtimestamp(
                os.path.getmtime(self.DATAFILE)
            )
            next_update = last_modified + self.refresh_interval
            if next_update > now:
                logger.debug(f'Will refresh at {next_update}.')
                await asyncio.sleep((next_update - now).total_seconds())
            try:
                end_time = datetime.datetime.now()
                min_time = end_time - self.data_time_interval
                start_time = max(min_time, last_modified)
                data = await self.load_trade_data_from_dune(start_time, end_time)
                self.data = [
                    d
                    for d in data
                    if dateutil.parser.parse(d['block_time']) >=
                    min_time
                ]
                self.dump_trade_data_to_disk()
            except RuntimeError as err:
                logger.error(f"Exception loading data from dune: {err}. Retrying ...")


"""

gas_stats_collector = GasStatsCollector()
asyncio.run(gas_stats_collector.initialize())
gas_stats_collector.load_trade_data_from_disk()
with traced_context(logger, 'computing stats'):
    print(gas_stats_collector.compute_stats('Uniswap_2', '0x1343'))
"""
