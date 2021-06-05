#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Subclass Square"""
    def __init__(self, size):
        """Initializa method"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """String return from class Rectangle"""
        return "[Square] {}/{}".format(self.__size, self.__size)
