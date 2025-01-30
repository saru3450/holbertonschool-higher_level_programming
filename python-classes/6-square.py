#!/usr/bin/python3
'''
Define a Square
'''


class Square:
    '''Represents a square'''

    def __init__(self, size=0, position=(0, 0)):
        '''Initialize the square'''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''Getter for size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Setter for size'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        '''Getter for position'''
        return self.__position

    @position.setter
    def position(self, value):
        '''Setter for position'''
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''Return the current square area'''
        return self.__size * self.__size

    def my_print(self):
        '''Print the square with # and handle position'''
        if self.__size == 0:
            print()
            return

        # Print vertical spaces
        [print() for _ in range(self.__position[1])]

        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
