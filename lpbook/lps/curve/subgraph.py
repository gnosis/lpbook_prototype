from sgqlc.operation import Operation
from .artifacts.graphql_schema import graphql_schema as schema

from lpbook.thegraph.subgraph import GraphQLClient

from functools import partial

import asyncio
import aiohttp

class CurveGraphQLClient(GraphQLClient):
    url = 'https://api.thegraph.com/subgraphs/name/curvefi/curve'

    def __init__(self, session: aiohttp.ClientSession):
        super().__init__(self.url, session)

    def set_pool_state_fields(self, pool):
        pool.id()
        pool.coins().index()
        pool.coins().balance()
        pool.coins().token().id()
        pool.coins().token().symbol()
        pool.coins().token().decimals()
        pool.a()
        pool.fee()
        pool.admin_fee()

    def set_pool_id_field(self, pool):
        pool.id()
        pool.name()

    async def get_pools_page(self, pools_filter, field_setter, last_id, first, **kwargs):
        op = Operation(schema.Query)
        pools_filter = {**pools_filter}
        if last_id is not None:
            pools_filter.update({"id_gt": last_id})

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
        return self.paginated_on_id(partial(self.get_pools_page, pools_filter, field_setter, **kwargs))

    async def get_last_block(self):
        op = Operation(schema.Query)
        meta = op._meta()
        meta.block()
        meta.block().number()
        meta.block().hash()
        data = await self.get_data(op, '_meta')
        query = op + data
        return query._meta.block if hasattr(query, '_meta') else None
