#!/usr/bin/python3
''' the object is an instance of a class that inherited '''



def inherits_from(obj, a_class):
    ''' the function inherits_from '''
    return not type(obj) is a_class and isinstance(obj, a_class)
