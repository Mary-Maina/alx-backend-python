#!/usr/bin/env python3
""" Module Documentation """
from typing import Tuple, Union


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    """func doc"""
    return (k, v**2)
