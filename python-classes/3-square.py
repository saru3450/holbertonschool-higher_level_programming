#!/usr/bin/python3
'''
define a Square
'''


class Square:
    '''Empty classe Square'''

    def __init__(self, size=0):
        '''Private instance with size'''

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        '''
        returns the current square area
        '''
        return (self.__size * self.__size)
