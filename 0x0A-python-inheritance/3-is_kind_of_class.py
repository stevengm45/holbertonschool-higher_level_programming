#!/usr/bin/python3
"""This Function return True if the objects is an instance"""


def is_kind_of_class(obj, a_class):
    """return True if object is an instace or
    if the object is an instace of a class that inherited """
    return isinstance(obj, a_class)
