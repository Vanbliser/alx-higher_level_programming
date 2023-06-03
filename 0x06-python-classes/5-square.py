#!/usr/bin/python3

"""Contains a class Square.

"""


class Square:
    """A class square."""

    def __init__(self, size=0):
        """constructor to initialize a class."""
        self.size = size

    @property
    def size(self):
        """property getter size

        size must be an integer. If size is less than 0, raise an exception
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not (isinstance(value, int)):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """area of a suare.

        Returns:
            the area of square
        """
        return (self.size)**2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.size == 0:
            print()
        else:
            for col in range(self.size):
                print('#'*(self.__size))
