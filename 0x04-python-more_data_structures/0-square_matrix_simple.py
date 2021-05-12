#!/usr/bin/python
def square_matrix_simple(matrix=[]):
    copy = []
    for i in matrix:
        copy.append(list(map(lambda x: x ** 2, i)))
    return copy
