#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """function that prints a text with 2 new lines after each
    of these caracters: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = "".join([word if word not in ".?:"
                 else word + '\n\n' for word in text])
    print('\n'.join([j.strip() for j in i.split('\n')]), end="")
