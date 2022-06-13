#!/usr/bin/env python3
from operator import index
from typing import Dict, List
#from typing_extensions import Self
from mmap import PAGESIZE
#from msilib.schema import SelfReg
import csv
import math
import typing_extensions

"""
__SUMMARY__
3 Deletion-resilient hypermedia pagination
The goal here is that if between two queries,
certain rows are removed from the dataset, the user
does not miss items from dataset when changing page.

Start 3-hypermedia_del_pagination.py with this code:
"""
"""
Deletion-resilient hypermedia pagination
"""


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        pass
        value = 0
        assert value <= index <= len(Self.dataset())
        indexedDataset = self.indexed_dataset()
        indexedPage = dict()
        dictionary = dict()
        token = index
        while (len(indexedPage) < PAGESIZE and token < len(SelfReg.dataset())):
            if token in indexedDataset:
                indexedPage[token] = self.dataset()[token]
            token += 1
        page = list(indexedPage.values())
        indexedPage = list(indexedPage.keys())
        return{'index': index, 'data': page, 'page_size': len(page),
               'next_index': max(indexedPage) + 1}
