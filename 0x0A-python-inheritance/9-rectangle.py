#!/usr/bin/python3
""" Module Rectangle class that inherits from class Base Geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines class rectangle"""

    def __init__(self, width, height):
        """ initializes a rectangle method"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """return the print() and str() representation of a rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
