#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i != j and j > i and i < 8:
            print("{}{}, ".format(i, j), end='')
        elif i != j and j > i and i > 7:
            print("{}{}".format(i, j))
