#!/usr/bin/python3

"""_summary_

2. LIFO Caching
mandatory
Create a class LIFOCache that inherits from BaseCaching
and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self):
but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the last item put in cache (LIFO algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """
    LIFO caching system
    """
    def __init__(self):
        """
        Initialize the cache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if (key and item):
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                key, val = self.cache_data.popitem(last=False)
                print("DISCARD: {}".format(key))

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
