#!/usr/bin/env python3
from typing import Tuple, Union
"""
   Defines a module that implements a function  to_kv that takes a
   list[float] input_list as argument and returns the string
   representation of the list[float]
"""


def to_kv(k: str, v: Union[int, float], ) -> Tuple[str, float]:
    """
    Args:
        input_list (list[float]): The number list.

    Returns:
        tuple: A tuple with elements k and v.
    """
    return (k, v * v)
