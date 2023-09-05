#!/usr/bin/python3
"""contains a function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """a function that finds a peak in a list of unsorted integers."""
    length = len(list_of_integers)
    if length == 0:
        return
    if length == 1:
        return list_of_integers[0]
    if length == 2:
        if list_of_integers[1] >= list_of_integers[0]:
            return list_of_integers[1]
        return list_of_integers[0]
    if length == 3:
        if (list_of_integers[1] > list_of_integers[0]
                and list_of_integers[1] > list_of_integers[2]):
            return list_of_integers[1]
        if (list_of_integers[0] >= list_of_integers[2]):
            return list_of_integers[0]
        return list_of_integers[2]
    a = length // 3
    b = length - (2 * a) + 1
    p1 = find_peak(list_of_integers[:a])
    p2 = find_peak(list_of_integers[a:b])
    p3 = find_peak(list_of_integers[b:])
    if p2 > p1 and p2 > p3:
        return p2
    if p1 >= p3:
        return p1
    return p3
