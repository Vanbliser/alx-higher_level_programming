#!/usr/bin/python3
k = 0
for i in range(9):
    k += 1
    for j in range(k, 10):
        if (i == 8 and j == 9):
            print("{0}{1}".format(i, j))
        else:
            print("{0}{1}".format(i, j), end=", ")
