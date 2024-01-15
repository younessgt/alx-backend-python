#!/usr/bin/env python3
"""script conatin wait_random function """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ function that takes in an integer argument and
    wait for a random delay between 0 and max_delay seconds
    and eventually returns it"""

    randnm_delay = random.uniform(0, max_delay)
    await asyncio.sleep(randnm_delay)
    return randnm_delay
