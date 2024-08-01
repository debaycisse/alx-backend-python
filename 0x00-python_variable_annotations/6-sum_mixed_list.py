#!/usr/bin/env python3
"""
This modules houses the definition of a function,
named sum_mixed_list whose dicumentation is given below
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums up a list of both integer and float numbers

    Args:
        mxd_lst - a list variable that contains both integer and float types

    Returns:
        the total value of all the numbers
    """
    total: float = 0.0
    for num in mxd_lst:
        total += num
    return total
