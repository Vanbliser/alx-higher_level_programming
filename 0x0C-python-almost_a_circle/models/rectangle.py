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
        if (not isinstance(value, int)) or (not issubclass(int, type(value))):
            raise TypeError("width must be an integer")
        if value == value+1:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """property height"""
        return self.__height

    @height.setter
    def height(self, value):
        if (not isinstance(value, int)) or (not issubclass(int, type(value))):
            raise TypeError("height must be an integer")
        if value == value+1:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """property x"""
        return self.__x

    @x.setter
    def x(self, value):
        if (not isinstance(value, int)) or (not issubclass(int, type(value))):
            raise TypeError("x must be an integer")
        if value == value+1:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """property y"""
        return self.__y

    @y.setter
    def y(self, value):
        if (not isinstance(value, int)) or (not issubclass(int, type(value))):
            raise TypeError("y must be an integer")
        if value == value+1:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """method that returns the area of this rectangle"""
        return self.width * self.height

    def display(self):
        """print in stdout the rectangle instance with #"""
        for y in range(self.y):
            print()
        for i in range(self.height):
            print(self.x*" ", self.width*"#", sep="")

    def __str__(self):
        """string representation"""
        a = self.__class__.__name__
        b = self.id
        c = self.x
        d = self.y
        e = self.width
        f = self.height
        return f"[{a}] ({b}) {c}/{d} - {e}/{f}"

    def update(self, *args, **kwargs):
        """method that assigns arguments to each attribute"""
        if len(args) < 0 and len(kwargs) < 0:
            pass
        else:
            vals = [self.id, self.width, self.height, self.x, self.y]
            keys = {"id": 0, "width": 1, "height": 2, "x": 3, "y": 4}
            if len(args) > 0:
                for index, arg in enumerate(args):
                    vals[index] = arg
            else:
                for key, value in kwargs.items():
                    vals[keys[key]] = value
            self.id, self.width, self.height, self.x, self.y = vals
