#!/usr/bin/python3
"""contain a class Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class Square"""
    def __init__(self, size):
        """class constuctor"""
        super().integer_validator("size", size)
        super().__init__(size, size)
