#!/usr/bin/python3
"""Class Mylist that inherits from list"""

class MyList(list):
    """Funcion to print sorted list"""
    def print_sorted(self):
        """print sorted"""
        print(sorted(self))
