#!/usr/bin/python3
"""Module 5-text_indentation
"""


def text_indentation(text):
    """Function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
        text (str): must be a string
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] in [".", ":", "?"]:
            print("{}".format(text[i]))
            print()
            i = i + 1
        else:
            print("{}".format(text[i]), end="")
        i = i + 1
