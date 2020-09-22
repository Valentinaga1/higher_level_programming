#!/usr/bin/python3
"""Documentation for a square class"""


class Square():
    '''class Square.
    '''

    def __init__(self, size=0):
        '''Initialization of instance attributes
                Args:
                size (int): The size of the square
        '''
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

# TypeError: When the value passed in is not an integer
# ValueError: When the value passed in is less than 0
