#!/usr/bin/python3
"""contain a class Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class Square"""
    def __init__(self, size):
        """class constuctor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
