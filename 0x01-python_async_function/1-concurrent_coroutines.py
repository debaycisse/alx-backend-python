#!/usr/bin/env python3
"""This module houses the definiton of
a coroutine function, named wait_n"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int):
    """Spawns wait_ramdom coroutine in a times

    Args:
        n - number of times to spawn the wait_random coroutine
        max_delay - the given delay or time it takes
        each execution of the coroutine

    Returns:
        the list of the coroutine
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return tasks
