#!/usr/bin/env python3
''' Complex types - string and int/float to tuple'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' This function takes a str and int/float args
    to return them as a tuple'''
    return (k, float(v**2))
