#!/usr/bin/env python3
""" script to_kv function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ function that takes a string k and
    an int OR float v as arguments and returns a tuple"""
    square: float = v**2
    return (k, square)
