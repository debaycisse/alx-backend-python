#!/usr/bin/env python3
"""
This module houses a definition of an annotated function
"""

from typing import Tuple, List, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequence (which may be a list or tuple or string)

    Args:
        lst - holds an iterable set of sequences

    Returns:
        a list of tuple where each tuple contains both a sequence
        and its length
    """
    return [(i, len(i)) for i in lst]
