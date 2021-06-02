#!/usr/bin/python3
"""This function creat a class"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """Initializing instance variables"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrives the dict representation of the class"""
        dict = {}
        if type(attrs) == list:
            for i in attrs:
                if type(i) != str:
                    dict = self.__dict__
                    break
                try:
                    dict[i] = getattr(self, i)
                except:
                    pass
        else:
            dict = self.__dict__
        return dict

    def reload_from_json(self, json):
        """Replace all attributes of student instance"""
        for key, val in json.items():
            self.__setattr__(key, val)
