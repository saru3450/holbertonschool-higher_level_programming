#!/usr/bin/python3

""" Module that defines a function that returns the
    list of available attributes and methods of an object"""


class BaseGeometry:
    """ BaseGeometry class """
    def area(self):
        """ raises an Exception with the message area() is not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
