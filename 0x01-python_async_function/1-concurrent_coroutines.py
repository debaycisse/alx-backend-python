#!/usr/bin/env python3
"""This module houses the definiton of
a coroutine function, named wait_n"""

import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    wait_random = __import__('0-basic_async_syntax').wait_random
    """Spawns wait_ramdom coroutine in a times

    Args:
        n - number of times to spawn the wait_random coroutine
        max_delay - the given delay or time it takes
        each execution of the coroutine

    Returns:
        the list of the coroutine
    """
    results = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    for com_task in asyncio.as_completed(tasks):
        res = await com_task
        results.append(res)
    return results
