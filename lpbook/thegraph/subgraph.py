import asyncio
import logging

import aiohttp

from ..util.aiohttp_endpoint import AIOHTTPEndpoint

logger = logging.getLogger(__name__)


class GraphQLClientError(RuntimeError):
    pass


class GraphQLClient:
    page_size = 500

    def __init__(self, url, session: aiohttp.ClientSession):
        self.endpoint = AIOHTTPEndpoint(self.url, session)

    def paginated(self, query):
        """Abstracts the fact that results are paginated."""
        cur_page_size = self.page_size
        cur_skip = 0
        while cur_page_size == self.page_size:
            cur_page = query(skip=cur_skip, first=self.page_size)
            cur_page_size = len(cur_page)
            cur_skip += cur_page_size
            for i in cur_page:
                yield i

    # Apparently this is now the preferred way to do pagination
    async def paginated_on_id(self, query):
        """Abstracts the fact that results are paginated."""
        cur_page_size = self.page_size
        last_id = None
        while cur_page_size == self.page_size:
            cur_page = await query(first=self.page_size, last_id=last_id)
            if len(cur_page) == 0:
                break
            cur_page_size = len(cur_page)
            for i in cur_page:
                yield i
            last_id = cur_page[-1].id

    async def get_data(self, op, must_have_key=None, keep_trying=False):
        while True:
            data = await self.endpoint(op)

            if 'errors' not in data.keys() and (
                must_have_key is None or must_have_key in data['data'].keys()
            ):
                break
            if not keep_trying:
                raise GraphQLClientError(
                    f'Error accessing thegraph: {str(data["errors"])}'
                )
            logger.warn(
                'Error getting data from graphql endpoint. Retrying in 2 secs ...'
            )
            logger.debug('errors: ' + str(data['errors']))
            await asyncio.sleep(2)
        return data
