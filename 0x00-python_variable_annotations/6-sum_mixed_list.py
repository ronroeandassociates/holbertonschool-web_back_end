#!/usr/bin/env python3
"""
6 Complex types - mixed list

a type-annotated function sum_mixed_list which takes a list mxd_lst
of integers and floats and returns their sum as a float

functions:
    sum_mixed_list(mxd_lst: list) -> float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Return the sum of all the floats in input_list.
    """
    return float(sum(mxd_lst))
