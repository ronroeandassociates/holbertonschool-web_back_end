#!/usr/bin/env python3
"""
  9 Let's duck type an iterable object

Annotate the below function’s parameters and return values with the appropriate types

def element_length(lst):
    return [(i, len(i)) for i in lst]

Functions:
    def element_length(lst: Iterable) -> List[Tuple[str, int]]:
"""
from typing import Iterable,Sequence,List,Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples of the form (element, length).
    """
    return [(i, len(i)) for i in lst]
