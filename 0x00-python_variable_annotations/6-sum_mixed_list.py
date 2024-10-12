#!/usr/bin/env python
""" Module Documentation"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """func doc"""
    total: float = 0.00
    for i in mxd_lst:
        total += i
    return total
