#!/usr/bin/env python3
"""
Task 1's modules
"""


BaseCaching = __import__("base_caching").BaseCaching


class BasicCaching(BaseCaching):
    """BasicCache class
    """

    def put(self, key, item):
        """ Must assign to the directory base.cache_data the item value for
        the key, if key or item is None then take no action
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ return the value in self.cache_data linked to key.
        If key is None or dosent exists, return  None
        """
        return self.cache_data.get(key, None)
