from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional, Union

from web3.exceptions import ContractLogicError

from ..util import Token


def create_token_from_web3(address, web3_client):
    with open(Path(__file__).parent / 'artifacts' / 'erc20.abi', 'r') as f:
        erc20_contract_abi = f.read()
        erc20 = web3_client.eth.contract(abi=erc20_contract_abi, address=address)

    try:
        symbol = erc20.functions.symbol().call()
    except (ContractLogicError, OverflowError):
        symbol = ''
    try:
        decimals = erc20.functions.decimals().call()
    except ContractLogicError:
        decimals = 18

    return Token(address=address.lower(), symbol=symbol, decimals=decimals)


@dataclass
class BlockId:
    """Identifies a block.

    If both number and hash are None, then it identifies the latest block.
    """

    number: Optional[int] = None
    hash: Optional[str] = None

    def __hash__(self):
        return self.hash

    @classmethod
    def latest(cls):
        return BlockId(number=None, hash=None)

    def is_fully_qualified(self):
        return self.number is not None and self.hash is not None

    def with_number(self, number: int):
        return BlockId(hash=self.hash, number=number)

    def __str__(self) -> str:
        if self.number is None and self.hash is None:
            return '<latest>'
        elif self.number is not None and self.hash is not None:
            return f'{self.number}/{self.hash[:8]}'
        elif self.hash is not None:
            return self.hash[:8]
        else:
            return str(self.number)

    @classmethod
    def from_web3(cls, block) -> "BlockId":
        return BlockId(number=block.number, hash=block.hash.hex())

    def to_web3(self) -> str:
        if self.hash is not None:
            return self.hash
        elif self.number is not None:
            return self.number
        else:
            return 'latest'

    def to_thegraph_filter(self) -> Dict:
        block = {}
        if self.hash is not None:
            block.update(hash=self.hash)
        elif self.number is not None:
            block.update(number=self.number)
        if len(block) > 0:
            return {'block': block}
        return {}
