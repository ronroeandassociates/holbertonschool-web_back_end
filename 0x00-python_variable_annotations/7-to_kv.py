#!/usr/bin/env python3
"""_summary_
  7 Complex types - string and int/float to tuple

Write a type-annotated function to_kv that takes a string k and
an int OR float v asarguments and returns a tuple. The first
element of the tuple is the string k The second element is the
square of the int/float v and should be annotated as a float

Functions:

  to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return the tuple (k, v**2).
    """
    return (k, v**2)
