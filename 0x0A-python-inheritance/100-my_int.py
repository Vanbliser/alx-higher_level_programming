#!/usr/bin/python3
"""contain MyInt class"""

class MyInt(int):
    """class MyInt"""

    def __eq__(self, other):
        return int(self) != int(other)

    def __ne__(self, other):
        return int(self) == int(other)
