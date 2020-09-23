#!/usr/bin/python3
"""Documentation for a square class"""


class Square():
    '''class Square.
    '''
    # Creating instance
    def __init__(self, size=0, position=(0, 0)):
        '''Initialization of instance attributes
            Args:
            size (int): The size of the square
            position (int): Coordenadas
        '''
        self.size = size
        self.position = position

    # Property. Instance atribute private
    @property
    def size(self):
        '''
            property  to retrieve it
        '''
        return self.__size

    @size.setter
    # setter
    def size(self, value):
        '''
            property  setter to set it
            Args:
            value(int)
        '''
        if type(value) != int:
                raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    # Property. atribute public insctance
    @property
    def position(self):
        '''
        property  to retrieve it
        '''
        return self.__position

    # setter
    @position.setter
    def position(self, value):
        '''
            property  setter to set it
            Args:
            value(int)
        '''
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''
            Method that returns the current square area
        '''
        return self.__size**2

    def my_print(self):
        '''
            Method that prints in stdout the square with
            the character #
        '''
        if self.__size is 0:
            print()
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print((" " * self.__position[0]) + ("#" * self.__size))
