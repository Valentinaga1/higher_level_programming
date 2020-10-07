#!/usr/bin/python3
import json
""""Module to define a JSON representation string function
"""


def save_to_json_file(my_obj, filename):
    """Function that writes an Object to a text file, using a JSON representation:

    Args:
        my_obj : object to convert to json
        filename (str): text file to read.
    """
    with open("my_obj.json", 'w+') as f:
        json.dump(my_obj, f)
