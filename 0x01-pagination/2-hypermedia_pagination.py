#!/usr/bin/env python3
"""
__Summary__
2 Hypermedia pagination
Replicate code from the previous task.

Classes:
    Server

Functions:
    dataset(self) -> List[List]
    get_page(self, int, int) -> List[List]
    index_range(self, int, int) -> Tuple[int, int]
    get_hyper(self, int, int) -> dict

"""
import csv
import math
from typing import List, Dict
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return page of the dataset
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        page, page_size = index_range(page, page_size)
        try:
            return self.dataset()[page:page_size]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Return page of the dataset"""

        listpage = self.get_page(page, page_size)

        total_pages = math.ceil(len(self.dataset()) / page_size)

        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None
        page_size = 0 if listpage == [] else page_size

        return {'page_size': len(listpage),
                'page': page,
                'data': listpage,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages}
