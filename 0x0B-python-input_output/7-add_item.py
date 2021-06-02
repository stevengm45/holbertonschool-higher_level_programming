#!/usr/bin/python3
"""Script adds all arguments to a python list"""


from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    elements_list = load_from_json_file("add_item.json")
except:
    elements_list = []

for elements in (argv[1:]):
    elements_list.append(elements)
    save_to_json_file(elements_list, "add_item.json")
