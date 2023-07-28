#!/usr/bin/python3

from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """
    Create a class LFUCache that inherits from BaseCaching
    and is a caching system
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.cache_order = OrderedDict()

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item value for the key
        """
        if key is not None and item is not None:

            if key in self.cache_data:
                self.cache_data.pop(key)
                self.cache_order.pop(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                oldest = next(iter(self.cache_order))
                self.cache_data.pop(oldest)
                self.cache_order.pop(oldest)
                print("DISCARD: {}".format(oldest))

            self.cache_data[key] = item
            self.cache_order[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key
        """
        if key is not None and key in self.cache_data:
            self.cache_order.move_to_end(key)
            return self.cache_data.get(key)
        return None
