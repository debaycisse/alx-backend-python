#!/usr/bin/env python3
"""
This module houses a definition of a function, named make_multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float, generates a function that takes the float and returns it

    Args:
        multiplier - the float to be used by the function

    Returns:
        a function that takes the multiplier and multiply by itself
    """
    def inner_multiplier(num: float) -> float:
        """
        This inner function gets returned

        Args:
            num - the value to multiply with the multiplier variable

        Returns:
            the value of the multiplication of the num and multiplier
        """
        return (multiplier * num)
    return inner_multiplier
