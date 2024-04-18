#!/usr/bin/env python3
'''Defines a module with an annotated function and values'''
from typing import Iterable, List, Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Returns None values'''
    if lst:
        return lst[0]
    else:
        return None
