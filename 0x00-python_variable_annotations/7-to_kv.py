#!/usr/bin/env python3
"""
This module contains the definition of a function, named to_kv
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and an integer or float and converts them into a tuple

    Args:
        k - variable that holds a string data
        v - variable that holds an integer or float
    """
    return ((k, v ** 2))
