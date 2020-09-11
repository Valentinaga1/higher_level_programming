#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = {}
    for key in a_dictionary:
        b_dictionary[key] = a_dictionary.get(key) * 2
    return b_dictionary

# Another way: dict compreh
# return {key: a_dictionary[key] * 2 for key in a_dictionary}
# así a_dictionary[key] accedo al dic en cada key para traer el value
# si no accedo al valor obtengo solo la key

# Another way
# return {key: 2 * v for key, v in a_dictionary.items()}
# .item devuelve una lista de tuplas clave valor
# estoy iterando sobre la key y el value
# le estoy poniendo la misma clave * 2
