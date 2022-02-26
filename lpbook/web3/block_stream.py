from abc import abstractmethod, abstractproperty
import asyncio
import json
import logging
import os
from typing import Set
from web3 import Web3

from websockets import connect

logger = logging.getLogger(__name__)


class BlockScanning:
    """A set of methods that need to exist on any streams/proxies scanning blocks."""

    @abstractproperty
    def block_hashes(self) -> Set[str]:
        """Returns all block hashes we are sure we have scanned."""

    @abstractproperty
    def block_numbers(self) -> Set[int]:
        """Returns all block number we are sure we have scanned."""

    @abstractproperty
    def last_block_number(self) -> int:
        """Most recent block number scanned."""

    @abstractproperty
    def last_block_hash(self) -> str:
        """Most recent block hash scanned."""

    @abstractmethod
    def get_block_number_from_hash(self, block_hash):
        """Get block number from block hash."""


class BlockStream(BlockScanning):
    """Maintains a table of block number/hashes from a given block onwards."""

    def __init__(self, web3_ws):
        """web3_ws should be a node websocket endpoint"""
        self.web3_ws = web3_ws
        self.subscribers = []
        self._last_block_number = None
        self._last_block_hash = None
        self.running = False
        self.block_number_by_hash = {}

    def get_block_number_from_hash(self, block_hash):
        return self.block_number_by_hash[block_hash]

    @property
    def block_hashes(self) -> Set[str]:
        return set(self.block_number_by_hash.keys())

    @property
    def block_numbers(self) -> Set[int]:
        return set(self.block_number_by_hash.values())

    @property
    def last_block_number(self) -> int:
        return self._last_block_number

    @property
    def last_block_hash(self) -> str:
        return self._last_block_hash

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    async def trigger(self, block_number, block_hash):
        self.block_number_by_hash[block_hash] = block_number
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
        on each block in [start_block_number, current_block_number[
        """
        self.running = True
        if start_block_number is not None:
            w3 = Web3(Web3.WebsocketProvider(self.web3_ws))
            while True:
                latest_block_number = w3.eth.get_block_number()
                if start_block_number == latest_block_number:
                    break
                assert start_block_number < latest_block_number
                start_block = w3.eth.get_block(start_block_number)
                logger.debug(f"Telling subscribers about past block {start_block_number}/{start_block.hash.hex()[:8]}")
                await self.trigger(start_block.number, start_block.hash.hex())
                start_block_number += 1

        logger.debug(f"{self} has finished processing past blocks")
        async with connect(self.web3_ws) as ws:
            await ws.send(json.dumps({"id": 1, "method": "eth_subscribe", "params": ["newHeads"]}))
            subscription_response = await ws.recv()

            # TODO: How to validate that subscription was correct?
            assert "id" in json.loads(subscription_response).keys()

            while True:
                message = await ws.recv()
                message = json.loads(message)
                block_number = int(message["params"]["result"]["number"], base=16)
                block_hash = message["params"]["result"]["hash"]
                logger.debug(f"Detected new block {block_number}/{block_hash[:8]}. Telling subscribers about it ...")
                await self.trigger(block_number, block_hash)

    async def run(self, start_block_number: int = None):
        """Listens for new blocks and calls subscribers on each of them.

        If start_block_number is not None, then it will first call subscribers
        on each block in [start_block_number, current_block_number[
        """
        logger.debug(f"Starting {self} ...")
        try:
            await self.run_helper(start_block_number)
        except Exception as err:
            logger.error(
                f"Error in {self}: {err}. "
            )
            import traceback
            traceback.print_exc()
        finally:
            logger.debug(f"Stopping {self} ...")
