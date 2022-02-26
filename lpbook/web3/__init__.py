from dataclasses import dataclass
from pathlib import Path
from typing import Union

from web3.exceptions import ContractLogicError

from ..util import Token


def create_token_from_web3(address, web3_client):
    with open(Path(__file__).parent / "artifacts" / "erc20.abi", "r") as f:
        erc20_contract_abi = f.read()
        erc20 = web3_client.eth.contract(abi=erc20_contract_abi, address=address)

    try:
        symbol = erc20.functions.symbol().call()
    except ContractLogicError:
        symbol = ""
    try:
        decimals = erc20.functions.decimals().call()
    except ContractLogicError:
        decimals = 18

    return Token(address=address.lower(), symbol=symbol, decimals=decimals)


# Following web3 convention, can be 'latest', a block number, or a block hash.
BlockDescriptor = Union[str, int]

@dataclass
class Block:
    number: int
    hash: str

    def __hash__(self):
        return self.hash
