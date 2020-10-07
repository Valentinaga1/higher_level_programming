#!/usr/bin/python3
"""Module to define a function to return number of lines of text file.
"""


def number_of_lines(filename=""):
    """Function that returns the number of lines of a text file

    Args:
        filename (str): text file to read.

    Returns:
        int: Number of lines of text file
    """
    count = 0
    with open(filename, 'r') as reader:
        for i in reader:
            count += 1
    return count
