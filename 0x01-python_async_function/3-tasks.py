#!/usr/bin/env python3
"""This module houses the defintion of a
function, named task_wait_random"""

import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """takes a number and returns a Task object

    Args:
        max_delay - maximum value of the range of value to delay

    Returns:
        an asyncio.Task object
    """
    val = random.uniform(0, max_delay)
    return asyncio.create_task(wait_random(val))
