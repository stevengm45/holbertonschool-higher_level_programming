#!/usr/bin/python3
"""This function read a file UTF8"""
def read_file(filename=""):
    """Reads file UTF-8"""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
