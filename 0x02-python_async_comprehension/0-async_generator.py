#!/usr/bin/env python3
""" script contain async_generator function """

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ asynchronus generator that yield a number for each iteration"""
    for i in range(11):
        await asyncio.sleep(1)
        random_number = random.uniform(0, 10)
        yield random_number
