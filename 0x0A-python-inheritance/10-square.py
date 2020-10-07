#!/usr/bin/python3
"""Module that writes an empty class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Rectangle(BaseGeometry):
    """Creating class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square (Rectangle):
    """Creating class Square that inherits from Rectangle
    """
    def __init__(self, size):
        Rectangle.__init__(self, size, size)
