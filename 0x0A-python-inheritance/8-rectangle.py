#!/usr/bin/python3
"""Module that writes an empty class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Creating class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """Initializes data

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
