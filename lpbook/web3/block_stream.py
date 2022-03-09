from abc import abstractproperty
import asyncio
import json
import logging
from web3 import Web3

from websockets import connect

from lpbook.util import traced

logger = logging.getLogger(__name__)


class BlockScanning:
    """A set of methods that need to exist on any streams/proxies scanning blocks."""

    @abstractproperty
    def last_block_number(self) -> int:
        """Most recent block number scanned."""

    @abstractproperty
    def last_block_hash(self) -> str:
        """Most recent block hash scanned."""


class BlockStream(BlockScanning):
    """Maintains a table of block number/hashes from a given block onwards."""

    def __init__(self, web3_ws):
        """web3_ws should be a node websocket endpoint"""
        self.web3_ws = web3_ws
        self.subscribers = []
        self._last_block_number = None
        self._last_block_hash = None
        self.running = False

    @property
    def last_block_number(self) -> int:
        return self._last_block_number

    @property
    def last_block_hash(self) -> str:
        return self._last_block_hash

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    async def trigger(self, block_number, block_hash):
        self._last_block_number = block_number
        self._last_block_hash = block_hash
        await asyncio.gather(
            *[
                subscriber(block_number, block_hash)
                for subscriber in self.subscribers
            ]
        )

    async def run_helper(self, start_block_number: int = None):
        """Listens for new blocks and calls subscribers on each of them.

        If start_block_number is not None, then it will first call subscribers
        on each block in [start_block_number, current_block_number[.
        """
        self.running = True
        if start_block_number is not None:
            w3 = Web3(Web3.WebsocketProvider(self.web3_ws))
            while True:
                latest_block_number = w3.eth.get_block_number()
                if start_block_number > latest_block_number:
                    break
                assert start_block_number <= latest_block_number
                start_block = w3.eth.get_block(start_block_number)
                logger.debug(
                    f'Telling subscribers about past block {start_block_number}'
                    f'/{start_block.hash.hex()[:8]}'
                )
                await self.trigger(start_block.number, start_block.hash.hex())
                start_block_number += 1

        logger.debug(f'{self} has finished processing past blocks')
        async with connect(self.web3_ws) as ws:
            await ws.send(json.dumps({
                'id': 1,
                'method': 'eth_subscribe',
                'params': ['newHeads']
            }))
            subscription_response = await ws.recv()

            # TODO: How to validate that subscription was correct?
            assert 'id' in json.loads(subscription_response).keys()

            while True:
                message = await ws.recv()
                message = json.loads(message)
                block_number = int(message['params']['result']['number'], base=16)
                assert start_block_number is None or block_number >= start_block_number
                # this avoids a notifying twice about the same block, which can happen
                # when "stitching" the processing of past blocks above with this loop.
                if start_block_number is not None and block_number == start_block_number:
                    continue
                block_hash = message['params']['result']['hash']
                logger.debug(
                    f'Detected new block {block_number}/{block_hash[:8]}. '
                    'Telling subscribers about it ...'
                )
                await self.trigger(block_number, block_hash)

    @traced(logger, 'Running BlockStream')
    async def run(self, start_block_number: int = None):
        """Listens for new blocks and calls subscribers on each of them.

        If start_block_number is not None, then it will first call subscribers
        on each block in [start_block_number, current_block_number[
        """
        await self.run_helper(start_block_number)
