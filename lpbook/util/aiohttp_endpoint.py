"""This file provides asyncio support for sgqlc. 

Adapted from https://github.com/profusion/sgqlc/discussions/162#discussioncomment-1040386
"""

import json
import logging
from contextlib import asynccontextmanager
from typing import Dict, Optional, Union

import aiohttp
from aiohttp.client_exceptions import ClientResponseError
from sgqlc.endpoint.base import BaseEndpoint, add_query_to_url

logger = logging.getLogger(__name__)

class AIOHTTPEndpoint(BaseEndpoint):

    def __init__(
        self,
        url: str,
        session: aiohttp.ClientSession,
        base_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[int] = None,
        method: str = "POST",
    ):
        self.url = url
        self.base_headers = base_headers or {}
        self.timeout = timeout
        self.method = method
        self.session = session

    def __str__(self):
        return (
            "%s(url=%s, base_headers=%r, timeout=%r, " "method=%s, session=%s)"
        ) % (  # noqa
            self.__class__.__name__,
            self.url,
            self.base_headers,
            self.timeout,
            self.method,
            self.session.__class__,
        )

    async def __call__(
        self,
        query: Union[bytes, str],
        variables: Optional[Dict] = None,
        operation_name: Optional[str] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[int] = None,
    ):
        if isinstance(query, bytes):
            query = query.decode("utf-8")
        elif not isinstance(query, str):
            # allows sgqlc.operation.Operation to be passed
            # and generate compact representation of the queries
            query = bytes(query).decode("utf-8")

        headers = self.base_headers.copy()
        if extra_headers:
            headers.update(extra_headers)

        if "Accept" not in headers:
            headers["Accept"] = "application/json; charset=utf-8"

        if self.method.upper() == "POST":
            get_http_request = self.get_http_post_request
        else:
            get_http_request = self.get_http_get_request

        req = get_http_request(
            query,
            variables,
            operation_name,
            headers,
            timeout,
        )

        logger.debug("Query:\n%s", query)

        try:
            async with req() as response:
                try:
                    response.raise_for_status()
                    data: Optional[Dict] = await response.json()
                    if data and data.get("errors"):
                        return self._log_graphql_error(query, data)
                    return data
                except json.JSONDecodeError as exc:
                    return self._log_json_error(await response.text(), exc)
        except aiohttp.ClientResponseError as exc:
            return self._log_http_error(exc)

    def get_http_post_request(
        self,
        query: Union[bytes, str],
        variables: Optional[Dict] = None,
        operation_name: Optional[str] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[int] = None,
    ):
        post_data = json.dumps(
            {
                "query": query,
                "variables": variables,
                "operationName": operation_name,
            }
        ).encode("utf-8")
        headers.update(
            {
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": str(len(post_data)),
            }
        )

        @asynccontextmanager
        async def post_request():
            async with self.session.post(
                url=self.url,
                data=post_data,
                headers=headers,
                timeout=timeout or self.timeout,
            ) as response:
                yield response
        return post_request

    def get_http_get_request(
        self,
        query: Union[bytes, str],
        variables: Optional[Dict] = None,
        operation_name: Optional[str] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[int] = None,
    ):
        params = {"query": query}
        if operation_name:
            params["operationName"] = operation_name

        if variables:
            params["variables"] = json.dumps(variables)

        url = add_query_to_url(self.url, params)

        @asynccontextmanager
        async def get_request():
            async with self.session.get(
                url=url, headers=headers, timeout=timeout or self.timeout
            ) as response:
                yield response

        return get_request

    def _log_http_error(self, exc: ClientResponseError):
        logger.error("%s: %s", exc.request_info.real_url, exc)
        for h in sorted(exc.headers):
            logger.info("Response header: %s: %s", h, exc.headers[h])

        return {
            "data": None,
            "errors": [
                {
                    "message": str(exc),
                    "exception": exc,
                    "status": exc.code,
                    "headers": exc.headers,
                }
            ],
        }
