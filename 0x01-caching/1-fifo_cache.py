#!/usr/bin/env python3
"""  A module implement a caching class (FIFO) """

from collections import OrderedDict
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class """

    def __init__(self):
        """ Initialize the class """

        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache """

        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            print(f"DISCARD: {first_key}")
            self.cache_data.pop(first_key)

    def get(self, key):
        """ Get an item by key """

        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
