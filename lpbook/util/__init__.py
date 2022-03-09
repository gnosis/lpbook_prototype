from abc import abstractproperty
import asyncio
from contextlib import contextmanager
from dataclasses import dataclass
from typing import List, Dict

import functools
import time


@contextmanager
def traced_context(logger, description):
    start_time = time.perf_counter()
    logger.debug(f'{description} ...')
    yield
    end_time = time.perf_counter()
    run_time = end_time - start_time
    logger.debug(f'{description} ... done ({run_time:.4f} secs)')


def traced(logger, description=None):
    """Logs calls to the decorated function."""
    def traced_decorator(func):
        nonlocal description
        if description is None:
            description = f'{func.__name__!r}'

        @functools.wraps(func)
        def sync_wrapper(*args, **kwargs):
            with traced_context(logger, description):
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    logger.debug(f'Caught exception in {func.__name__!r}: {err}')
                    raise err

        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            with traced_context(logger, description):
                try:
                    return await func(*args, **kwargs)
                except Exception as err:
                    logger.debug(f'Caught exception in {func.__name__!r}: {err}')
                    raise err

        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        else:
            return sync_wrapper

    return traced_decorator


@dataclass
class Token:
    address: str
    symbol: str
    decimals: int

    def __hash__(self):
        return self.address.__hash__()


class LP:
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
    elif hasattr(obj, '_ast'):
        return to_dict(obj._ast())
    elif hasattr(obj, '__iter__') and not isinstance(obj, str):
        return [to_dict(v, classkey) for v in obj]
    elif hasattr(obj, '__dict__'):
        data = dict([
            (key, to_dict(value, classkey))
            for key, value in obj.__dict__.items()
            if not callable(value) and not key.startswith('_')
        ])
        if classkey is not None and hasattr(obj, '__class__'):
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
        assert(False)   # TODO: fill in more cases
