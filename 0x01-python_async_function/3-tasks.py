#!/usr/bin/env python3
""" script conatin task_wait_random function """

import asyncio
from asyncio import Task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """ function that return a asyncio.Task"""

    obj = asyncio.create_task(wait_random(max_delay))
    return obj
