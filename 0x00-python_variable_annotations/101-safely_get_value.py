#!/usr/bin/env python3
'''Defines a module with an annotated function and values'''
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    '''
    Returns a dct element or default value.

    Args:
        dst (Mapping): The input Mapping.

    Returns:
        [Any | T]: A default or a dct item.
    '''
    if key in dct:
        return dct[key]
    else:
        return default
