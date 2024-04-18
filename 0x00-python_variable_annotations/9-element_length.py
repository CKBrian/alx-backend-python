#!/usr/bin/env python3
from typing import Iterable, List, Sequence, Tuple
'''Defines a module with an annotated function and values'''


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a tuple.

    Args:
        lst (Iterable[Sequence]): The input iterable containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each containg an
        element from the input list and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
