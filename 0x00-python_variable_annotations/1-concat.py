#!/usr/bin/env python3
"""
This modules houses the definition of a function, named concat
"""


def concat(str1: str, str2: str) -> str:
    """
    Adds two given string together by concatenating them

    Args:
        str1 - variable that holds the first string
        str2 - variable that holds the second string

    Returns:
        the concatenated version is returned
    """
    return "{}{}".format(str1, str2)
