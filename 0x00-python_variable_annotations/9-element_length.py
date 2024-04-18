#!/usr/bin/env python3
from typing import Iterable, List, Sequence, Tuple
'''Defines a module with an annotated function and values'''

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]

