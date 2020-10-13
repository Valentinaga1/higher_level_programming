#!/usr/bin/python3
"""Module that defines the class Rectangle that inherits from Base class
"""

from models.base import Base


class Rectangle(Base):
    """Class Rectangle that ihnerits from base

    Args:
        Base : Super class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Create a Rectangle instance
        """
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @width.setter
    def width(self, width):
        """Setter for width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """Setter for height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """Setter for x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """Setter for y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Defining public method area"""
        return self.__width * self.__height

    def display(self):
        """Defining public method to display a rectangle with "#" """
        print("\n" * self.__y, end="")
        for i in range(self.__height):
                print(" " * self.__x, end="")
                print("#" * self.__width)

    def __str__(self):
        """Defining str method to print"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Defining public method to variable arguments"""
        if len(args) > 0:
            for key, value in enumerate(args):
                if key == 0:
                    self.id = value
                elif key == 1:
                    self.width = value
                elif key == 2:
                    self.height = value
                elif key == 3:
                    self.x = value
                elif key == 4:
                    self.y = value
        else:
            if "id" in kwargs:
                self.id = kwargs['id']
            if "width" in kwargs:
                self.width = kwargs['width']
            if "height" in kwargs:
                self.height = kwargs['height']
            if "x" in kwargs:
                self.x = kwargs['x']
            if "y" in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """Defining public method to returns the representation
        of a dictionary"""
        dictionary = {}
        dictionary['id'] = self.id
        dictionary['width'] = self.width
        dictionary['height'] = self.height
        dictionary['x'] = self.x
        dictionary['y'] = self.y
        return dictionary
