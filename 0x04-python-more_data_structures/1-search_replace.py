#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy = my_list.copy()
    for i, j in enumerate(copy):
        if j == search:
            copy[i] = replace
    return copy
