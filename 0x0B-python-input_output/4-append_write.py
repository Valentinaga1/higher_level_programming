#!/usr/bin/python3
"""Module to define a file appending string function.
"""


def append_write(filename="", text=""):
    """Function that appends a string at the end of a text file

    Args:
        filename (str): text file to read.
        text (str): string to be writte.

    Returns:
        int: number of characters added
    """
    with open(filename, 'a') as f:
        return f.write(text)
