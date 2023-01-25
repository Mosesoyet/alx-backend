#!/usr/bin/env python3
"""
Task 0's module
"""
import csv
import math
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size 2 containing a start index 
    and an end index corresponding to the range of indexs 
    to return in a list for those particular pagination parameters
    """
    start_index, end_index = 0, 0
    for i in range(page):
        start_index = end_index
        end_index += page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate database
    of popular baby name
    """
     DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        dataset page
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        dataset = self.dataset()
        data_length = len(dataset)
        try:
            index = index_range(page, page_size)
            return dataset[index[0]:index[1]]
        except IndexError:
            return []
