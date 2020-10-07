#!/usr/bin/python3
"""Module that lists attributes and methods of an object
"""


def lookup(obj):
    """Function hat returns the list of available attributes and methods of
    an object

    Args:
        obj : the object

    Returns:
        [list]: list of atributes and methods
    """
    return dir(obj)
