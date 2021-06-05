#!/usr/bin/python3
""" Class Square that inherits from Rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ subclass Square inherits from Rectangle"""
    def __init__(self, size):
        """initializa method"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
