#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    else:
        return max(a_dictionary, key=a_dictionary.get)

# Another way:
# if a_dictionary:
#  dict_ord = sorted(a_dictionary.items(), key=lambda k_v: k_v[1])
#   if a_dictionary.get(dict_ord[-1][0]):
#     return dict_ord[-1][0]
#    return
# sorted( lista clave valor, key =especifico cómo orgnizarlo)
# aquí estoy org por clave por eso k_v[1]
