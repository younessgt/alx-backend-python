#!/usr/bin/env python3
""" script contain async_generator function """

import asyncio
import random
from typing import Generator, AsyncGenerator
# mypy inform that the return type hint should be
# AsyncGenerator instead of Generator
# But alx have another view


async def async_generator() -> Generator[float, None, None]:
    """ asynchronus generator that yield a number for each iteration"""
    for _ in range(10):
        await asyncio.sleep(1)
        random_number = random.uniform(0, 10)
        yield random_number
