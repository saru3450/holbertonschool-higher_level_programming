#!/usr/bin/python3
"""
This module contains a function that adds two integers.
2
3
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
