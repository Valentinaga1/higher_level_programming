#!/usr/bin/python3
"""Module that defines a class Rectangle
"""


class Rectangle:
    """Defining class Rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiation of Rectangle.

        Args:
            width (int): width of the Rectangle.
            height (int,): height of the Rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''
            Method that returns the current rectangle area
        '''
        return (self.__height * self.__width)

    def perimeter(self):
        '''
            Method that returns the current rectangle perimeter
        '''
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2 + self.__width * 2)

    def __str__(self):
        string = ""
        if self.__width == 0 or self.__height == 0:
            return("")
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    string = string + str(self.print_symbol)
                if i < self.__height - 1:
                    string = string + '\n'
            return string

    def __repr__(self):
        class_name = self.__class__.__name__
        return "{}({}{})".format(class_name, self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
