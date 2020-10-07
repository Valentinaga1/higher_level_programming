#!/usr/bin/python3
"""Module to define a function that returns a dictionary description.
"""


def class_to_json(obj):
    """Function that returns the dictionary description with simple data
    structure

    Args:
        obj : instance of a Class

    Returns:
        Returns de dictionary description
    """
    return obj.__dict__
