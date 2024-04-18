#!/usr/bin/env python3
"""
   Defines a module that implements a function make_multiplier that takes a
   list[float | int] multiplier as argument and returns the string
   representation of the list[float]
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Args:
        multiplier (float): The float number.

    Returns:
        callable[[float], float]:  `multiplier` function that multiplies
        two float numbers.
    """
    def multiply(num: float) -> float:
        """Returns the product of two float numbers"""
        return multiplier * num
    return multiply
