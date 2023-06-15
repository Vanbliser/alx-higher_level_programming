#!/usr/bin/python3
"""contains a class Rectangle"""


class Rectangle:
    """ a class Rectangle that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Rectangle class constructor

        Args:
            width (int): width of the rectangle. Defaults to 0
            heigth (int): higth of the rectangle. Defaults to 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value == value+1:
            raise TypeError("width must be an integer")
        if isinstance(value, bool):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if isinstance(value, bool):
            raise TypeError("height must be an integer")
        if value == value+1:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
