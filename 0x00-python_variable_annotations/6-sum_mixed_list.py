#!/usr/bin/env python3
"""
   Defines a module that implements a function  sum_mixed_list that takes a
   list[float | int] mxd_lst as argument and returns the string
   representation of the list[float]
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Args:
        mxd_lst (list[float | int]): The number list.

    Returns:
        float: The sum  of `mxd_lst` elements.
    """
    return sum(mxd_lst)
