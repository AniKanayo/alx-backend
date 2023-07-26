#!/usr/bin/env python3
"""
This module contains a LIFOCache class
"""

from base_caching import BaseCaching
from collections import deque


class LIFOCache(BaseCaching):
    """
    LIFOCache class. It is a caching system with a LIFO
    discarding algorithm. It inherits from BaseCaching.
    """

    def __init__(self):
        """
        Initialize the LIFOCache class
        """
        super().__init__()
        self.order = deque()

    def put(self, key, item):
        """
        Assign the item value for the key in self.cache_data
        dictionary.If key or item is None, this method will do nothing.
        If the number of items in self.cache_data is higher than
        BaseCaching.MAX_ITEMS, discard the last item put in cache
        (LIFO algorithm) and print 'DISCARD: ' with the key discarded.
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    discarded = self.order.pop()
                    del self.cache_data[discarded]
                    print(f"DISCARD: {discarded}")
                self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        If key is None or if the key doesn't exist in self.cache_data,
        return None.
        """
        return self.cache_data.get(key, None)
