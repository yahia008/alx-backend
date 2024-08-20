#!/usr/bin/env python3
"""FIFO (First-In, First-Out) caching system.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Describes an object that enables storing and,
    retrieving items from a dictionary, employing,
    a FIFO (First In, First Out) eviction policy,
    when it reaches its capacity limit.
    """
    def __init__(self):
        """Sets up the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Stores an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Fetches an item using its key.
        """
        return self.cache_data.get(key, None)
