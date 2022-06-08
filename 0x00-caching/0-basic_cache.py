#!/usr/bin/python3

"""_summary_
0 Basic dictionary

Create a class BasicCache that inherits from BaseCaching and
is a caching system:

You must use self.cache_data - dictionary from the
parent class BaseCaching this caching system doesnt have limit
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value
for the key key.
If key or item is None, this method should not do anything.
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesnt exist in self.cache_data,
return None
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Basic caching system
    """
    def __init__(self):
        """
        Initialize the cache
        """
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache
        """
        if key is None:
            return None
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
