#!/usr/bin/python3
"""Contains matrix_divided function"""


def matrix_divided(matrix, div):
    """a function that divides all elements of a matrix.

    Args:
        matrix (list): a list of list of elements of type int/float
        div (int:float): a integer or float, not equal to zero

    Raises:
        TypeError: if matrix is not a list of list of type int/float,
            if each list in the list is not same size
        ZeroDivisionErro: if div equals zero
    """
    result = list()
    i = float('inf')
    j = float('-inf')
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not check(div):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list):
        raise TypeError(msg)
    if len(matrix) < 1:
        raise TypeError(msg)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg)
        if len(matrix[0]) != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        if len(row) < 1:
            raise TypeError(msg)
        if not all(list(map(lambda x: check(x), row))):
            raise TypeError(msg)
        result.append(list(map(lambda x: round(x/div, 2), row)))
    return result


def check(x):
    """a function that checks if x is not infinity or a large number
    and if x is an instance of int or float

    Args:
        x (int:float) the value to check

    Returns:
        return True if not infinity or large number else False
    """
    if x == float('inf'):
        return False
    if x == float('-inf'):
        return False
    if not isinstance(x, (int, float)):
        return False
    if x == x+1:
        return False
    return True
