#!/usr/bin/python3
"""Module that checks if an object is an instance of a class
"""


def is_same_class(obj, a_class):
    """Function that returns True if the object is exactly an instance
    of the specified class or false if is not

    Args:
        obj : Object
        a_class : Class

    Returns:
        True or False
    """
    return type(obj) is a_class
