#!/usr/bin/env python3
"""
This module house the definition of a function, named safe_first_element
"""

from typing import Any, Sequence, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Takes a list and return its first element

    Args:
        lst - the variable that holds data of the list

    Returns:
        Either none or the first element is returned
    """
    if lst:
        return lst[0]
    else:
        return None
