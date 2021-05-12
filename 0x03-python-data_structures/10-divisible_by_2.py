#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    pares = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            pares.append(True)
        else:
            pares.append(False)
    return pares
