#!/usr/bin/python3
"""Define class Rectangle"""


class Rectangle:
    """Representation od a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Inizializes the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """print a string whe an instance has been deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
            string += '\n'.join(str(self.print_symbol) * self.__width
                                for i in range(self.__height))
        return string

    def __repr__(self):
        """returns a string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance od Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
