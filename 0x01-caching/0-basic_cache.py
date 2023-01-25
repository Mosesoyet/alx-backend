#!/usr/bin/env python3
""" 
0. Basic dictionary
"""


BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    ''' 
    BasicCache class. Inherits from BaseCaching.
    '''

    def put(self, key, value):
        ''' Must assign to the dictionary self.cache_data the item value for
        the key key. If key or item is None, this method should not do anything
        '''
        if key and value:
            self.cache_data[key] = value

    def get(self, key):
        '''
        Must return the value in self.cache_data linked to key. If key is
        None or if the key doesn’t exist in self.cache_data, return None.
        '''
        return self.cache_data.get(key, None)
