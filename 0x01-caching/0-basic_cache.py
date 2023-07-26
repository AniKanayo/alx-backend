#!/usr/bin/env python3
"""
This module contains a BasicCache class
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class. It is a caching system without a limit.
    It inherits from BaseCaching.
    """

    def put(self, key, item):
        """
        Assign the item value for the key in self.cache_data dictionary.
        If key or item is None, this method will do nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        If key is None or if the key doesn't exist in self.cache_data, return None.
        """
        return self.cache_data.get(key, None)
