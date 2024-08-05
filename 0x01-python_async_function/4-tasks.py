#!/usr/bin/env python3
"""This modules houses the definiton of a function, called task_wait_n"""

import asyncio
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    task_wait_random = __import__('3-tasks').task_wait_random
    """Spawns wait_ramdom coroutine in a times

    Args:
        n - number of times to spawn the wait_random coroutine
        max_delay - the given delay or time it takes
        each execution of the coroutine

    Returns:
        the list of the coroutine
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = []
    for com_task in asyncio.as_completed(tasks):
        res = await com_task
        results.append(res)
    return results
