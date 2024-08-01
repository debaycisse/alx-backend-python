#!/usr/bin/env python3
"""
This module contains a definition of a function, named sum_list
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Takes a list of float numbers and sums them up

    Args:
        input_list - a list of float number to be summed up

    Returns:
        the total value of the summation of all the element in the list
    """
    total: float = 0.0
    for num in input_list:
        total += num
    return total
