#!/usr/bin/python3
"""This module contains the Base class"""
import json


class Base:
    """Class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Inicialize the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
