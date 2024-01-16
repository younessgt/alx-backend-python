#!/usr/bin/env python3
"""script contain async_comprehension function """

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """function that collect 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers """
    final = [i async for i in async_generator()]
    return final
