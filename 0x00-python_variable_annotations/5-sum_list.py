#!/usr/bin/env python3
from typing import List
"""
   Defines a module that implements a function  sum_list that takes a
   list[float] input_list as argument and returns the string
   representation of the list[float]
"""


def sum_list(input_list: List[float]) -> float:
    """
    Args:
        input_list (list[float]): The number list.

    Returns:
        float: The sum  of `input_list` elements.
    """
    return sum(input_list)
