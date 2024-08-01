#!/usr/bin/env python3
"""
This module contains the definition of a funcation, named floor.
"""

import math


def floor(n: float) -> int:
    """
    Converts a given number to its nearest floor value by striping
    off its decimal value

    Args:
        n - variable that holds the number to be converted

    Returns:
        the converted equivalent of the given number
    """
    return math.floor(n)
