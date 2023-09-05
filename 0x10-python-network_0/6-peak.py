#!/usr/bin/python3
"""contains a function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """a function that finds a peak in a list of unsorted integers."""
    l = len(list_of_integers);
    if l == 0:
        return
    if l == 1:
        return list_of_integers[0]
    a = l // 2
    p1 = find_peak(list_of_integers[:a])
    p2 = find_peak(list_of_integers[a:])
    if p1 >= p2:
        return p1
    return p2
