#!/usr/bin/python3
"""
Module for LFUCache.
"""

from base_caching import BaseCaching
from collections import Counter


class LFUCache(BaseCaching):
    """
    LFUCache class. Inherits from BaseCaching.
    Uses caching system with least frequently used item (LFU algorithm)
    """

    def __init__(self):
        """
        Initialize.
        """
        super().__init__()
        self.frequency = Counter()

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if None not in {key, item}:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                least_common = self.frequency.most_common()[:-2:-1]
                if least_common:
                    self.cache_data.pop(least_common[0][0])
                    self.frequency.pop(least_common[0][0])
                    print(f"DISCARD: {least_common[0][0]}")

            self.cache_data[key] = item
            self.frequency[key] += 1

    def get(self, key):
        """
        Get an item by key
        """
        if key is not None and key in self.cache_data:
            self.frequency[key] += 1
            return self.cache_data.get(key)
        else:
            return None
