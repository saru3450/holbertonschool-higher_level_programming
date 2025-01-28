#!/usr/bin/python3
'''
define a Square
'''


class Square:
    '''Empty classe Square'''

    def __init__(self, size=0, position=(0, 0)):
        '''Private instance with size'''
        self.__size = size
        self.__position = position

    ''' Instantiation with optional '''
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        ''' stter of position'''
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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

    def my_print(self):
        '''
        Public instance method
        '''
        if self.__size == 0:
            print()
            return
        [print() for i in range(0, self.__position[1])]
        for i in range(self.__size):
           [print("#", end="") for item in range(0, self.__position[0])]
           [print("#", end="") for k in range(0, self.__size)]
           print ("")
