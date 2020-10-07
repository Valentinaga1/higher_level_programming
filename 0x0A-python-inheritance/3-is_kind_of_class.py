#!/usr/bin/python3
"""Module to cheks if an object is an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """Function that returns True if the object is an instance of, or if the
    object is an instance of a class that inherited from, the specified class

    Args:
        obj : Object
        a_class : Class

    Returns:
        True or False
    """
    return isinstance(obj, a_class)
