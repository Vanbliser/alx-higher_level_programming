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
        if not (isinstance(value, int) or isinstance(value, float)):
            raise TypeError('size must be a number')
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

    def __eq__(self, other):
        """implement equality

        Args:
            other (Suare): the other object of type Square to for equality
        """
        s = (self.size)**2
        o = (other.size)**2
        return s == o

    def __lt__(self, other):
        """implement less than

        Args:
            other (Square): the other object being compared with
        """
        s = (self.size)**2
        o = (other.size)**2
        return s < o

    def __le__(self, other):
        """implement less than or equal to

        Args:
            other (Square): the other object being compared with
        """
        s = (self.size)**2
        o = (other.size)**2
        return s <= o
