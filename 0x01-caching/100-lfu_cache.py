#!/usr/bin/env python3
"""  A module implement a caching class (LFU) """

BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class """

    def __init__(self):
        """ Initialize the class """

        super().__init__()
        self.frequency = {}
        self.recently_used = {}

    def put(self, key, item):
        """ Add an item in the cache """

        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.frequency.values())
                lfu_keys = [
                    k for k, v in self.frequency.items() if v == min_freq
                ]

                if len(lfu_keys) > 1:
                    lru_key = min(
                        lfu_keys,
                        key=lambda k: self.recently_used[k]
                    )
                else:
                    lru_key = lfu_keys[0]

                print(f"DISCARD: {lru_key}")
                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                del self.recently_used[lru_key]

            self.cache_data[key] = item
            self.frequency[key] = 1

        self.recently_used[key] = len(self.recently_used) + 1

    def get(self, key):
        """ Get an item by key """

        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.recently_used[key] = len(self.recently_used) + 1

        return self.cache_data[key]
