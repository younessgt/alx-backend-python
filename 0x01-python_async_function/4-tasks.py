#!/usr/bin/env python3
"""Script contain task_wait_n function"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ some function as wait_n but this uses task_ait)random function
    instead of creating manually here a tasks"""

    list_delay = []
    list_coroutine_obj = []

    for _ in range(n):
        coroutine_obj = task_wait_random(max_delay)
        list_coroutine_obj.append(coroutine_obj)

    for coroutine_obj in asyncio.as_completed(list_coroutine_obj):
        delay = await coroutine_obj
        list_delay.append(delay)
    return list_delay
