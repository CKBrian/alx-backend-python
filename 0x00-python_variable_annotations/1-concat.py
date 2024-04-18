#!/usr/bin/env python3
"""
   Defines a module that implements a function concat that takes a string
   str1 and a string str2 as arguments and returns a concatenated string
"""


def concat(str1: str, str2: str) -> str:
    """
    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        str: The concatenation of `str1` and `str2`.
    """
    return "{}{}".format(str1, str2)
