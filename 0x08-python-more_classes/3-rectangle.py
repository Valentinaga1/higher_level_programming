"""Module that defines a class Rectangle
"""


class Rectangle:
    """Defining class Rectangle
    """

    def __init__(self, width=0, height=0):
        """Instantiation of Rectangle.

        Args:
            width (int): width of the Rectangle.
            height (int,): height of the Rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getting width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setting width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getting height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setting height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            Method that returns the current rectangle area
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """
            Method that returns the current rectangle perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2 + self.__width * 2)

    def __str__(self):
        """
        Method to be used when use print on Rectangle
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return("")
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    string = string + "#"
                if i < self.__height - 1:
                    string = string + '\n'
            return string
