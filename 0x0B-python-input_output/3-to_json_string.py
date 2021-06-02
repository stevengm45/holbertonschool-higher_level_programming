#!/usr/bin/python3
"""This funcion return the JSON respresentation of an object(string)"""
import json


def to_json_string(my_obj):
    """convert to json"""
    i = json.dumps(my_obj)
    return i
