#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        total_elements = 0
        for i in range(x):
            print(my_list[i], end='')
            total_elements = total_elements + 1
        print('')
        return total_elements
    except:
        print('')
        return total_elements
