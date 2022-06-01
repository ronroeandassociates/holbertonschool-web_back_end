#!/usr/bin/env python3
"""
5 Complex types - list of floats

a type-annotated function sum_list which takes a list input_list of floats as
argument and returns their sum as a float

Functions:
    sum_list(input_list: list) -> float
"""
from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Return the sum of all the floats in input_list.
    """
    return sum(input_list)
