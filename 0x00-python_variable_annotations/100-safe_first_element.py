#!/usr/bin/env python3
"""script contain safe_first_element function"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """safe_first_element function take lst as argument of type Sequence"""
    if lst:
        return lst[0]
    else:
        return None
