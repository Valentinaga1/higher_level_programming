#!/usr/bin/python3
"""Module that defines the class Rectangle that inherits from Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that ihnerits from Rectangle
    Args:
        Rectangle : class that inherits from
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Create a Square instance
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Defining str method to print"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, size):
        """Setter for size"""
        self.height = size
        self.width = size

    def update(self, *args, **kwargs):
        """Defining public method to variable arguments"""
        if len(args) > 0:
            for key, value in enumerate(args):
                if key == 0:
                    self.id = value
                elif key == 1:
                    self.size = value
                elif key == 2:
                    self.x = value
                elif key == 3:
                    self.y = value
        else:
            if "id" in kwargs:
                self.id = kwargs['id']
            if "size" in kwargs:
                self.size = kwargs['size']
            if "x" in kwargs:
                self.x = kwargs['x']
            if "y" in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """Defining public method to returns the representation
        of a dictionary"""
        dictionary = {}
        dictionary['id'] = self.id
        dictionary['size'] = self.width
        dictionary['x'] = self.x
        dictionary['y'] = self.y
        return dictionary
