#!/usr/bin/python3
"""This function return an object respresented by a JSON string"""
import json


def from_json_string(my_str):
    """return object"""
    i = json.loads(my_str)
    return i
