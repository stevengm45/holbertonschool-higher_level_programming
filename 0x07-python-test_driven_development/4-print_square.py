#!/usr/bin/python3
"""print square"""


def print_square(size):
    """this function that prints a square with #"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is not float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
