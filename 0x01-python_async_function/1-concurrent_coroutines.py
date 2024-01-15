#!/usr/bin/env python3
"""Script contain wait_n function"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ fucntion  that takes in 2 int arguments n and max_delay
    and  return the list of all the delays
    The list of the delays should be in ascending order
    without using sort() because of concurrency."""

    list_delay = []
    list_coroutine_obj = []

    for _ in range(n):
        coroutine_obj = asyncio.create_task(wait_random(max_delay))
        list_coroutine_obj.append(coroutine_obj)

    for coroutine_obj in asyncio.as_completed(list_coroutine_obj):
        delay = await coroutine_obj
        list_delay.append(delay)
    return list_delay
