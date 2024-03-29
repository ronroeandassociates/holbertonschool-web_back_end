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
        constructor
        """
        super().__init__()
        self.all_keys = []

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data
        the item value for the key key.
        """

        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            to_discard = self.all_keys.pop()
            print(f"DISCARD: {to_discard}")
            del self.cache_data[to_discard]

        self.all_keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key
        """

        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
