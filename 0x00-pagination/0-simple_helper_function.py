#!/usr/bin/env python3
""" Task 0's module
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Return a tuple of size 2 containing a start index 
    and an end index corresponding to the range of indexs 
    to return in a list for those particular pagination parameters
    """
    start_index = 0
    end_index = 0
    for i in range(page):
        start_index = end_index
        end_index += page_size
    return (start_index, end_index)
