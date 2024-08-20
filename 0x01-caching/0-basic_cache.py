#!/usr/bin/env python3
"""Simple caching system.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Denotes an object that enables the storage,
    and retrieval of items in a dictionary."""
    def put(self, key, item):
        """Stores an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Fetches an item using a specific key.
        """
        return self.cache_data.get(key, None)
