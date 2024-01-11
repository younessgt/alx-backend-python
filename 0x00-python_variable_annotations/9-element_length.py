#!/usr/bin/env python3
"""script contain element_length"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ function that takes lst as argument
    it should be of type Iterable (list, tuple, etc) containing elements
    of type Sequence (strings, lists) and return a list of tuples"""
    return [(i, len(i)) for i in lst]
