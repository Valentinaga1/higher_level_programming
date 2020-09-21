#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    total_elements = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            total_elements = total_elements + 1
        except (ValueError, TypeError):
            continue
    print('')
    return total_elements

# ValueError: tipo correcto, pero val incorre( fuera de rango)
# TypeError: objeto de tipo incorrecto
