#!/usr/bin/python3
"""Module to define a file writting function.
"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file (UTF8)

    Args:
        filename (str): text file to read.
        text (str): string to be writte.

    Returns:
        int: the number of characters written
    """
    with open(filename, 'w+') as f:
        return f.write(text)
