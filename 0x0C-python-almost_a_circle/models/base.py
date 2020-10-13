#!/usr/bin/python3
"""Module that defines the class Base
"""

import json


class Base:

    """Constructor class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Create a Base instance

        Args:
            id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Defining a method that returns JSON string rep"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None or list_objs == []:
            Newlist = []
        else:
            Newlist = cls.to_json_string([obj.to_dictionary()
                                          for obj in list_objs])
        with open(cls.__name__ + ".json", "w") as myFile:
            myFile.write(Newlist)

    @staticmethod
    def from_json_string(json_string):
        """Defining a static method that returns a string from JSON rep"""
        if json_string is None or len(json_string) == 0:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(1, 3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Defining a class method that writes a JSON string rep"""
        try:
            with open("{}.json".format(cls.__name__), 'r') as f:
                list_dic = cls.from_json_string(f.read())
        except:
            list_dic = []
        newList = []
        for dic in list_dic:
            newList.append(cls.create(**dic))
        return newList
