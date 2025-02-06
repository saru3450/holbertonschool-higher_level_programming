#!/usr/bin/env python3
"""
Define a class CountedIterator :
In the constructor (__init__)
initialize two attributes: the iterator object
"""

class CountedIterator:
    """
    class countediterador
    """
    def __init__(self, item):
        self.iterator = iter(item)
        self.counter = 0

    def __next__(self):
        item = next(self.iterator)
        self.counter += 1
        return item

    def get_count(self):
        return self.counter
