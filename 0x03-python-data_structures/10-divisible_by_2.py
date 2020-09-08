#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for number in my_list:
        if number % 2 == 0:
            return True
        else:
            return False
