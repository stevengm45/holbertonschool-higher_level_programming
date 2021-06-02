#!/usr/bin/python3
"""This function append a string at the end of a text file UTF8"""


def append_write(filename="", text=""):
    """Append a string at the end of text file"""
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
