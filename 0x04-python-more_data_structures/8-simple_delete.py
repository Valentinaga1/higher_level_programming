#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        a_dictionary.pop(key)
    return(a_dictionary)

# anothe way
#   if a_dictionary.get(key) is not None:
#       del a_dictionary[key]
#   return a_dictionary
