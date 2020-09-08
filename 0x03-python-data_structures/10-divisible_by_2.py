#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for number in my_list:
        if number % 2 == 0:
            my_list = True
        else:
            my_list = False
    return my_list
