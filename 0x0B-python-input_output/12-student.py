#!/usr/bin/python3
""" Module that defines a clas Student
"""


class Student():
    """class Student that defines a student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):	
        dictionary = {}
        if type(attrs) == list:
            for i in attrs:
                    if type(attrs) == list and type(i) == str and i in self.__dict__.keys():
                        dictionary[i] = self.__dict__[i]
                    return dictionary
        else:
            return self.__dict__
