#!/usr/bin/python3
"""contains a function that finds a peak in a list of unsorted integers."""


def find_peak_old(list_of_integers):
    """a function that finds a peak in a list of unsorted integers."""
    length = len(list_of_integers)
    if length == 0:
        return
    if length < 4:
        return max(list_of_integers)
    a = length // 3
    b = length - (2 * a) + 1
    p1 = find_peak(list_of_integers[:a])
    p2 = find_peak(list_of_integers[a:b])
    p3 = find_peak(list_of_integers[b:])
    return max(p1, p2, p3)


def find_peak(list_of_integers):
    """a function that finds a peak in a list of unsorted integers."""
    def find_peak_recursive(arr, left, right):
        """a recursive function to find the peak"""
        if left == right:
            return arr[left]

        mid = (left + right) // 2

        if arr[mid] < arr[mid + 1]:
            return find_peak_recursive(arr, mid + 1, right)
        else:
            return find_peak_recursive(arr, left, mid)

    if len(list_of_integers) == 0:
        return None

    return find_peak_recursive(list_of_integers, 0, len(list_of_integers) - 1)
