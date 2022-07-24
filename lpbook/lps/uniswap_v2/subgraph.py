from sgqlc.operation import Operation
from .artifacts.graphql_schema import graphql_schema as schema

from lpbook.thegraph.subgraph import GraphQLClient

from functools import partial

import aiohttp


class UniV2GraphQLClient(GraphQLClient):
    def __init__(self, url: str, session: aiohttp.ClientSession):
        self.url = url
        super().__init__(self.url, session)

    def set_pair_id_and_tokens_fields(self, pair):
        pair.id()
        pair.token0().id()
        pair.token0().symbol()
        pair.token0().decimals()
        pair.token1().id()
        pair.token1().symbol()
        pair.token1().decimals()

    def set_pair_state_fields(self, pair):
        self.set_pair_id_and_tokens_fields(pair)
        pair.reserve0()
        pair.reserve1()

    async def get_pairs_page(self, pairs_filter, field_setter, last_id, first, **kwargs):
        op = Operation(schema.Query)
        pairs_filter = {**pairs_filter}
        if last_id is not None:
            pairs_filter.update({'id_gt': last_id})

        pairs = op.pairs(
            where=pairs_filter,
            first=first,
            **kwargs
        )

        if field_setter is None:
            field_setter = self.set_pair_state_fields

        field_setter(pairs)

        data = await self.get_data(op, 'pairs')
        query = op + data
        return query.pairs if hasattr(query, 'pairs') else []

    def get_pairs_state(self, pairs_filter=dict(), field_setter=None, **kwargs):
        return self.paginated_on_id(
            partial(self.get_pairs_page, pairs_filter, field_setter, **kwargs)
        )

    async def get_last_block(self):
        op = Operation(schema.Query)
        meta = op._meta()
        meta.block()
        meta.block().number()
        meta.block().hash()
        data = await self.get_data(op, '_meta')
        query = op + data
        return query._meta.block if hasattr(query, '_meta') else None
