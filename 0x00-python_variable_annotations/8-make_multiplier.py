#!/usr/bin/env python3
"""
8 Complex types - functions

a type-annotated function make_multiplier that takes a float multiplier as
argument and returns a function that multiplies a float by multiplier

Functions:
    make_multiplier(multiplier: float) -> Callable[[float], float]:
"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by multiplier.
    """
    def multiplier_function(n: float) -> float:
        """
        Return the product of n and multiplier.
        """
        return n * multiplier
    return multiplier_function
