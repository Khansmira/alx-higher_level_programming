#!/usr/bin/python3
"""
Writes a string to a text file (UTF-8)
"""


def write_file(filename="", text=""):
    """
    Returns the number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
