#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    max_value = None
    for i in my_list:
        if max_value is None or i > max_value:
            max_value = i
    return max_value
