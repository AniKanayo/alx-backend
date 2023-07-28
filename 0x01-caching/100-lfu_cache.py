#!/usr/bin/python3
"""
100-lfu_cache.py
Module which contains a LFUCache class
"""

from base_caching import BaseCaching
from collections import deque, Counter


class LFUCache(BaseCaching):
    """LFUCache class"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.keys = []
        self.counter = Counter()

    def put(self, key, item):
        """Set the item in cache"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS and key not in self.keys:
            discarded_key, _ = self.counter.most_common()[:-2:-1][0]
            del self.cache_data[discarded_key]
            self.keys.remove(discarded_key)
            print('DISCARD: {}'.format(discarded_key))

        if key in self.cache_data:
            self.keys.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            discarded_key = self.keys.popleft()
            del self.cache_data[discarded_key]

        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """Get an item by key"""
        if key in self.cache_data:
            self.counter[key] += 1
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache_data[key]
        return None
