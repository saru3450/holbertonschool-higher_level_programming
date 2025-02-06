#!/usr/bin/env python3
"""
Create a class named VerboseList :
inherits from the built-in list class.
"""


class VerboseList(list):
    """
    class
    """
    def append(self, item):
        print("Added [{}] to the list.".format(item))
        super().append(item)

    def extend(self, items):
        print("Extended the list with [{}] items.".format(len(items)))
        super().extend(items)

    def remove(self, item):
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, item=-1):
        print("Popped [{}] from the list.".format(self[item]))
        super().pop(item)
        return super().pop(item)
