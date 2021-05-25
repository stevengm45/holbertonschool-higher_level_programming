#!/usr/bin/python3
"""Define class Rectangle"""


class Rectangle:
    """Representation od a rectangle"""
    def __init__(self, width=0, height=0):
        """Inizializes the rectangle"""
        self.width = width
        self.height = height

    def __del__(self):
        """print a string whe an instance has been deleted"""
        print("Bye rectangle...")

    @property
    def width(self):
        """setter fot the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """getter fot the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """setter fot the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """getter fot the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """the rectangle area"""
        self.__area = self.__width * self.__height
        return self.__area

    def perimeter(self):
        """the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            self.__perimeter = 0
        else:
            self.__perimeter = (2 * self.__width) + (2 * self.__height)
        return self.__perimeter

    def __str__(self):
        """Returns string representacion od the rectangle with #"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += '\n'.join('#' * self.__width
                                for i in range(self.__height))
        return string

    def __repr__(self):
        """returns a string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
