#!/usr/bin/python3
"""
Defines a class Square that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A square that inherits from Rectangle.
    """
    def __init__(self, size):
        """
        Initializes a square with a given size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size * 2
