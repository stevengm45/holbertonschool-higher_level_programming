#!/usr/bin/python3
"""this function that creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """create an object from JSON file"""
    with open(filename) as f:
        return json.load(f)
