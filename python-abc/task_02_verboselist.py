#!/usr/bin/python3

class VerboseList(list):
    def append(self, item):
        print("Added [{}] to the list.".format(item))
        super().append(item)

    def extend(self, items):
        print("Extended the list with {} items.".format(items))
        super().extend(items)

    def remove(self, item):
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        print("Popped [{}] from the list.".format(index))
        return super().pop(index)
