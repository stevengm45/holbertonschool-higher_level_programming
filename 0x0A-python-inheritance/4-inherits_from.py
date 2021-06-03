#!/usr/bin/python3
"""Function that return True if object is an instance"""


def inherits_from(obj, a_class):
    """Return if the object is an instance, check for object"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
