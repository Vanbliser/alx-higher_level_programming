#!/usr/bin/python3
"""contains a class Rectangle"""


class Rectangle:
    """ a class Rectangle that defines a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Rectangle class constructor

        Args:
            width (int): width of the rectangle. Defaults to 0
            heigth (int): higth of the rectangle. Defaults to 0
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def area(self):
        """return the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return the perimeter of the rectangle"""
        if (self.__width == 0) or (self.__height == 0):
            return 0
        return 2*(self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """a method that returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        if rect_2.area() > rect_1.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size"""
        return Rectangle(width=size, height=size)

    def __str__(self):
        """defines the printable string for rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        width = f"{self.__width*str(self.print_symbol)}"
        result = ""
        for i in range(self.__height):
            result += width
            if i < (self.__height)-1:
                result += '\n'
        return result

    def __repr__(self):
        """define the offical representation of Rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """destructor of Rectangle"""
        if type(self).number_of_instances > 0:
            type(self).number_of_instances -= 1
        print("Bye rectangle...")
