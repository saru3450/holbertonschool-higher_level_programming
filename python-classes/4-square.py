#!/usr/bin/python3
'''
define a Square
'''


class Square:
    '''Empty classe Square'''

    def __init__(self, size=0):
        '''Private instance with size'''
        self.__size = size

        '''Getter and setter methods are not 100% Python'''
    @property
    def size(self):
        '''property getter'''
        return self.__size

    @size.setter
    def size(self, value):
        '''property sette'''

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        '''
        returns the current square area
        '''
        return (self.__size * self.__size)
