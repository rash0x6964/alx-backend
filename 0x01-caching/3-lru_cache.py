#!/usr/bin/env python3
"""  A module implement a caching class (LRU) """

BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class """

    def __init__(self):
        """ Initialize the class """

        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """ Add an item in the cache """

        if key is None or item is None:
            return

        if key in self.cache_data:
            self.access_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.access_order.pop(0)
            print(f"DISCARD: {lru_key}")
            del self.cache_data[lru_key]

        # Add or update the item in the cache
        self.cache_data[key] = item
        self.access_order.append(key)

    def get(self, key):
        """ Get an item by key """

        if key is None or key not in self.cache_data:
            return None

        self.access_order.remove(key)
        self.access_order.append(key)
        return self.cache_data[key]
