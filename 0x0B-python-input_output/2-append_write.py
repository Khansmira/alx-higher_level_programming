#!/usr/bin/python3
"""
Appends a string to end of file (UTF-8)
"""


def append_write(filename="", text=""):
    """
    Returns the numbers of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
