#!/usr/bin/python3
"""Contains a class Square that defines a square."""


class Square:
    """A class square."""

    def __init__(self, size=0):
        """the square class constructor.

        Args:
            size (int, optional): the size of the sqaure.
                size must be an integer
        """
        self.size_setter(size)

    def size_getter(self):
        """property to get size

        size must be an integer, otherwise raise a TypeError exception with
        the message size must be an integer. if size is less than 0,
        raise a ValueError exception with the message size must be >= 0
        """
        return self.__size

    def size_setter(self, size):
        if not (isinstance(size, int)):
            raise TypeError('size must be an integer')
        elif (size < 0):
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
