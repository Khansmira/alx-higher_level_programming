#!/usr/bin/python3
"""
This function reads a text file (UTF-8) and prints it's content  to stdout
"""


def read_file(filename=""):
    """
    prints content of the the text file  to stdout
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
