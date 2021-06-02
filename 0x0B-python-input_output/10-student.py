#!/usr/bin/python3
"""This function creat a class"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return (self.__dict__)
        else:
            attrs_dic = {}
            for i in attrs:
                if hasattr(self, i):
                    attrs_dic[i] = getattr(self, i)
            return attrs_dic
