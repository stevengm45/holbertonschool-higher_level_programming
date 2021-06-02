#!/usr/bin/python3
"""This function read a file UTF8 and read the number of letters"""


def write_file(filename="", text=""):
    """Write a file utf8"""
    with open(filename, 'w', encoding='utf-8') as f:
        return(f.write(text))
