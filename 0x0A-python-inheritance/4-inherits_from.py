#!/usr/bin/python3
"""Module to checks is an object is an instance of a class
that inherited from the specified class
"""


def inherits_from(obj, a_class):
    """Function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class

    Args:s
        obj : Object
        a_class : Class

    Returns:
        True or False
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
