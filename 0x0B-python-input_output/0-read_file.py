#!/usr/bin/python3
"""Module to define a file reading function.
"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str): text file to read .
    """
    with open(filename, 'r') as reader:
        print(reader.read(), end="")
