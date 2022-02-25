from abc import abstractproperty
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Token:
    address: str
    symbol: str
    decimals: int

    def __hash__(self):
        return self.address.__hash__()

class LP:
    #id: str
    #type: str
    #tokens: List[Token]
    #state: dict

    @abstractproperty
    def uid(self) -> str:
        """Returns a unique identifier for the LP (like its address)."""

    @abstractproperty
    def type(self) -> str:
        """Returns the type of lp (UniswapV2, Curve, etc.)."""

    @abstractproperty
    def tokens(self) -> List[Token]:
        """Returns a list of tokens pooled by this LP."""

    @abstractproperty
    def state(self) -> Dict:
        """Returns the internal state of the LP (e.g. the two reserves for uniswapV2)."""

# Recursively convert an object to a dict
# https://stackoverflow.com/questions/1036409/recursively-convert-python-object-graph-to-dictionary
def to_dict(obj, classkey=None):
    if isinstance(obj, dict):
        data = {}
        for (k, v) in obj.items():
            data[k] = to_dict(v, classkey)
        return data
    elif hasattr(obj, "_ast"):
        return to_dict(obj._ast())
    elif hasattr(obj, "__iter__") and not isinstance(obj, str):
        return [to_dict(v, classkey) for v in obj]
    elif hasattr(obj, "__dict__"):
        data = dict([(key, to_dict(value, classkey)) 
            for key, value in obj.__dict__.items() 
            if not callable(value) and not key.startswith('_')])
        if classkey is not None and hasattr(obj, "__class__"):
            data[classkey] = obj.__class__.__name__
        return data
    else:
        return obj

# Recursively wrap all numbers as string.
def stringify(obj):
    if isinstance(obj, dict):
        data = {}
        for (k, v) in obj.items():
            data[stringify(k)] = stringify(v)
        return data
    elif isinstance(obj, str):
        return obj
    elif isinstance(obj, float) or isinstance(obj, int):
        return str(obj)
    else:
        assert(False) # TODO: fill in more cases