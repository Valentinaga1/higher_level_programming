#!/usr/bin/python3
""""Module to define a JSON representation string function.
"""
import json



def to_json_string(my_obj):
    """Function that returns the JSON representation of an object (string)

    Args:
        my_obj : object to convert to json

    Returns:
        the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
