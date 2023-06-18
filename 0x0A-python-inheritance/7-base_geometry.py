#!/usr/bin/python3
"""contain BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """a method  that raises an Exception with the message
        area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """a method that validates value

        Args:
            name (str): a variable label
            value (int): supposed integer to validate
        """
        if not (isinstance(value, int) and issubclass(int, type(value))):
            raise TypeError(f"{name} must be an integer")
        if value == value+1:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
