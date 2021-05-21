#!/usr/bin/python3
"""class Square definition"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """Initializes a square

        Args:
            __size (int): size of a side od the square

        Returns: None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """calculates the square's area
        Returns:
          The area of the square
        """
        return (self.__size) ** 2
