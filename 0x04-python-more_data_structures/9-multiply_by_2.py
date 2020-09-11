#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = a_dictionary
    for key in a_dictionary:
        b_dictionary[key] = a_dictionary.get(key) * 2
    return b_dictionary

# Another way: dict compreh
# return {key: a_dictionary[key] * 2 for key in a_dictionary}
# Another way
# return {key: 2 * v for key, v in a_dictionary.items()}
