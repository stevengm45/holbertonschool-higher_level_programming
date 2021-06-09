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

    @staticmethod
    def to_json_string(list_dictionaries):
        """method json"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        namefile = cls.__name__ + ".json"
        list_ob = []
        if list_objs is not None:
            for i in list_objs:
                list_ob.append(cls.to_dictionary(i))
        with open(namefile, 'w') as f:
            f.write(cls.to_json_string(list_ob))

    @staticmethod
    def from_json_string(json_string):
        emptylist = []
        if json_string is None or not json_string:
            return emptylist
        else:
            list_1 = json.loads(json_string)
            return list_1

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        namefile = cls.__name__ + '.json'
        emptyl = []
        list_2 = []
        try:
            with open(namefile, mode='r', encoding='utf-8') as x:
                temp = x.read()
                emptyl = cls.from_json_string(temp)
                """List of dicts"""
                for i in emptyl:
                    temp2 = cls.create(**i)
                    list_2.append(temp2)
                return list_2
        except FileNotFoundError:
            return emptyl
