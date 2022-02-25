import logging
from typing import List
from async_timeout import asyncio

from web3._utils.events import get_event_data
from web3.datastructures import AttributeDict

logger = logging.getLogger(__name__)

def get_event_signature(event):
    event = event._get_event_abi()
    return f"{event['name']}({','.join(input['type'] for input in event['inputs'])})"

class EventNotifier:
    def __init__(self, event_callback_handler, events: List, contract_addresses: List[str], web3_client):
        self.event_callback_handler = event_callback_handler
        self.web3_client = web3_client
        self.contract_addresses = contract_addresses
        self.filters = {event: None for event in events}
        self.abis = {event: None for event in events}
        self.updated_once = False

    async def update(self):
        for event, filter in self.filters.items():
            abi = self.abis[event]
            if self.updated_once:
                new_entries = await asyncio.to_thread(filter.get_new_entries)
            else:
                new_entries = await asyncio.to_thread(filter.get_all_entries)
            self.updated_once = True
            for encoded_event in new_entries:
                decoded_event = get_event_data(self.web3_client.codec, abi, encoded_event)
                decoded_event = AttributeDict(decoded_event, removed=encoded_event.removed)
                self.event_callback_handler(decoded_event)

    def create_filter(self, event, from_block_number: int):
        signature_hash = self.web3_client.keccak(text=get_event_signature(event)).hex()
        filter_parameters = {
            "address": self.contract_addresses,
            "topics": [signature_hash]
        }
        if from_block_number is not None:
            filter_parameters['fromBlock'] = from_block_number
        filter = self.web3_client.eth.filter(filter_parameters)
        self.filters[event] = filter
        self.abis[event] = event._get_event_abi()

    def cancel_event(self, event):
        self.web3_client.eth.uninstall_filter(self.filters[event].filter_id)
        self.filters.pop(event)
        self.abis.pop(event)

    def cancel_all_events(self):
        for event in self.filters.keys():
            self.cancel_event(event)

    def start(self, from_block_number: int = None):
        if from_block_number is None:
            logger.debug(f"Starting {self} at current block ...")
        else:
            logger.debug(f"Starting {self} at block {from_block_number} ...")
        for event in self.filters.keys():
            self.create_filter(event, from_block_number)
        logger.debug(f"Starting {self} ... done")

    def stop(self):
        logger.debug(f"Stopping {self} ...")
        self.cancel_all_events()
