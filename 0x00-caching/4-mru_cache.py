#!/usr/bin/python3
"""
_summary_

4 MRU Caching

Create a class MRUCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self):
but dont forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the most recently used item (MRU algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesnt exist in self.cache_data, return None
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class
    Args:
        BaseCaching (class): Basic class for this class
    """
    def __init__(self):
        super().__init__()
        self.__keys = []

    def put(self, key, item):
        """put item into cache_data with MRU algorithm
        Args:
            key ([type]): key of dictionary
            item ([type]): item to insert in dictionary
        """
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.__keys:
            discard = self.__keys.pop()
            del self.cache_data[discard]
            print(f'DISCARD: {discard}')
        if key and item:
            if key not in self.__keys:
                self.__keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """get value of cache_data dictionary
        Args:
            key ([type]): key to search into cache_data
        """
        if not key or key not in self.cache_data:
            return None
        self.__keys.remove(key)
        self.__keys.append(key)
        return self.cache_data[key]
