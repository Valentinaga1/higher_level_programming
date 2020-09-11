#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)  # convierto a ser porq  tiene datos unicos
    sum = 0
    for num in new_list:
        sum += num
    return sum

# another way:
# return sum(set(my_list)) list compreh
