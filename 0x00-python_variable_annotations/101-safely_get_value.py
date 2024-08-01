#!/usr/bin/env python3
"""This module houses a definition of a function, named safely_get_value"""

from typing import Union, Mapping, Any, TypeVar

T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None) -> Union[Any, T]:
    """
    Finds a key in a given dictionary and returns it, if found

    Args:
        dct - the given dictionary to be searched through
        key - the key to be searched up for in the given dictionary
        default - the value to be returned if the given key is not found
    """
    if key in dct:
        return dct[key]
    else:
        return default
