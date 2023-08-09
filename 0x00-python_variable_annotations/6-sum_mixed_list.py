#!/usr/bin/env python3
''' Complex type - mixed list '''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' The function takes integer and float args to return float '''
    return float(sum(mxd_lst))
