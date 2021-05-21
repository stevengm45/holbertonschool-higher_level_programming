#!/usr/bin/python3
"""class Square definition"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """Initializes a square

        Args:
        size (int): size of a side od the square

        Returns: None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
