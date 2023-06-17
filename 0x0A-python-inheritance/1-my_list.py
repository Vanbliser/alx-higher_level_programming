#!/usr/bin/python3
"""contains MyList class"""


class MyList(list):
    """a class MyList that inherits from list"""
    def print_sorted(self):
        """a public instance method hat prints the list, but sorted (ascending
        sort). assume that all the elements of the list will be of type int.
        """
        print(sorted(self))
