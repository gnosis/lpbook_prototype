from sgqlc.operation import Operation
from .artifacts.graphql_schema import graphql_schema as schema

from lpbook.thegraph.subgraph import GraphQLClient

from functools import partial

import asyncio
import aiohttp


class UniV3GraphQLClient(GraphQLClient):
    url = 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3'

    def __init__(self, session: aiohttp.ClientSession):
        super().__init__(self.url, session)

    def set_pool_state_fields(self, pool):
        pool.id()
        pool.token0().symbol()
        pool.token0().id()
        pool.token0().decimals()
        pool.token1().symbol()
        pool.token1().id()
        pool.token1().decimals()
        pool.fee_tier()
        pool.liquidity()
        pool.sqrt_price()
        pool.tick()

    def set_pool_id_field(self, pool):
        pool.id()

    async def get_pools_page(self, pools_filter, field_setter, last_id, first, **kwargs):
        op = Operation(schema.Query)
        pools_filter = {**pools_filter}
        if last_id is not None:
            pools_filter.update({'id_gt': last_id})

        pools = op.pools(
            where=pools_filter,
            first=first,
            **kwargs
        )

        if field_setter is None:
            field_setter = self.set_pool_state_fields

        field_setter(pools)

        data = await self.get_data(op, 'pools')
        query = op + data
        return query.pools if hasattr(query, 'pools') else []

    def get_pools_state(self, pools_filter=dict(), field_setter=None, **kwargs):
        """Get pairs."""
        return self.paginated_on_id(
            partial(self.get_pools_page, pools_filter, field_setter, **kwargs)
        )

    async def get_ticks_page(self, ticks_filter, last_id, first, **kwargs):
        op = Operation(schema.Query)
        if last_id is not None:
            ticks_filter.update({'id_gt': last_id})
        ticks = op.ticks(
            where=ticks_filter,
            first=first,
            **kwargs
        )
        ticks.id()
        ticks.tick_idx()
        ticks.liquidity_net()

        data = await self.get_data(op, 'ticks')
        query = op + data
        return query.ticks if hasattr(query, 'ticks') else []

    def get_ticks(self, ticks_filter, **kwargs):
        """Get pool ticks."""
        # ticks_filter.update({'liquidity_net_gt': 0})
        return self.paginated_on_id(partial(self.get_ticks_page, ticks_filter, **kwargs))

    async def get_pool_state(self, pool_id, **kwargs):
        op = Operation(schema.Query)
        pool = op.pool(
            id=pool_id,
            **kwargs
        )

        self.set_pool_state_fields(pool)

        data = await self.get_data(op, 'pool')
        query = op + data
        return query.pool if hasattr(query, 'pool') else None

    async def get_pool_state_and_ticks(self, pool_id, **kwargs):
        async def collect_all_ticks():
            return [tick async for tick in self.get_ticks({'pool': pool_id}, **kwargs)]

        pool_ticks = await asyncio.gather(
            self.get_pool_state(pool_id, **kwargs),
            collect_all_ticks(),
        )
        pool, ticks = pool_ticks[0], pool_ticks[1]
        pool['ticks'] = ticks
        return pool

    async def get_pools_state_and_ticks(self, pools_filter, ticks_filter, **kwargs):
        pools = [
            pool
            async for pool in self.get_pools_state(
                pools_filter,
                field_setter=None,
                **kwargs
            )
        ]
        pool_ids = [pool.id for pool in pools]

        ticks_filter = {**ticks_filter}
        ticks_filter.update(pool_in=pool_ids)
        ticks = [tick async for tick in self.get_ticks(ticks_filter, **kwargs)]

        def get_pool_id_from_tick(tick):
            return tick.id[:42]

        ticks_by_pool = {}
        for tick in ticks:
            pool_id = get_pool_id_from_tick(tick)
            if pool_id not in ticks_by_pool.keys():
                ticks_by_pool[pool_id] = []
            ticks_by_pool[pool_id].append(tick)

        for pool in pools:
            pool['ticks'] = ticks_by_pool.get(pool.id, [])

        return pools

    async def get_last_block(self):
        op = Operation(schema.Query)
        meta = op._meta()
        meta.block()
        meta.block().number()
        meta.block().hash()
        data = await self.get_data(op, '_meta')
        query = op + data
        return query._meta.block if hasattr(query, '_meta') else None
