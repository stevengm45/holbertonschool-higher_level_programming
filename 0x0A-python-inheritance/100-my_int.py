#!/usr/bin/python3
""" Class MyInt that that inherist"""


class MyInt(int):
    """subclass MyInt"""
    def __init__(self, x):
        """initializa method"""
        self.x = x

    def __eq__(self, other):
        return self.x != other

    def __ne__(self, other):
        return self.x == other
