#!/usr/bin/env python3
"""
This module houses the definition of well annotated function, named zoom_array
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    zooms a tuple by duplicating each element in a number of the
    value of factor whose default value is 2

    Args:
        lst - the tuple that contains the elements that are to be zoomed
        factor - the number of time each element is to be duplicated (zoomed)

    Returns:
        the zoomed or duplicated verion of the tuple's
        element in a list format
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
