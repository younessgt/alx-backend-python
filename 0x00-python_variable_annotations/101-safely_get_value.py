#!/usr/bin/env python3
""" script contain safely_get_value function """
from typing import Union, Mapping, Any, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ returning dct[key]  or default """
    if key in dct:
        return dct[key]
    else:
        return default
