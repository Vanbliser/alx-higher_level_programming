#!/usr/bin/python3
"""contains a Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """a Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """property width"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """property height"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """property x"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """property y"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
