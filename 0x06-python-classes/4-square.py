#!/usr/bin/python3
"""Documentation for a square class"""


class Square():
    '''class Square.
    '''
    # creating the instance
    def __init__(self, size=0):
        '''Initialization of instance attributes
            Args:
            size (int): The size of the square
        '''
        self.__size = size

    # public instance. Returns the area
    def area(self):
        return self.__size*self.__size

    # instance atribute private. Returns area
    @property
    def size(self):
        return self.__size

    # setter
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
