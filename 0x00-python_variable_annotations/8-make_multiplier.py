#!/usr/bin/env python3
""" script contain make_multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ function that takes a float multiplier as argument and
    returns a function that multiplies a float by multiplier"""
    return lambda m: m * multiplier
