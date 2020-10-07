#!/usr/bin/python3
"""Module to define a file reading function
"""


def read_lines(filename="", nb_lines=0):
    """Function that reads n lines of a text file (UTF8) and prints it to
    stdout:

    Args:
        filename (str): text file to read.
        nb_lines (int): number of lines
    """
    with open(filename, 'r') as reader:
        if nb_lines <= 0:
            print(reader.read())
        else:
            for line in range(nb_lines):
                print(reader.readline(), end="")
