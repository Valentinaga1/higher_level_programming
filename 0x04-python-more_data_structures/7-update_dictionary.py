#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    # si la key no existe la crea, si si la reemplaza
    return a_dictionary

# Another way
# a_dictionary.update(dict([(key, value)]))
# return a_dictionary
