#!/usr/bin/python3
"""Module that prints a sorted list
"""


class MyList(list):
    """Creatin MyList class that inherits form list

    Args:
        list (list): list to print
    """
    def print_sorted(self):
        print(sorted(self))
