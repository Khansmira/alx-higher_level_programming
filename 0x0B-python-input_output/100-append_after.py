#!/usr/bin/python3
"""
This function inserts a line of text after each line
containing the search string in a file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert text after each line containing a given string in a file
    """
    text = ""
    with open(filename) as x:
        for line in x:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as f:
        f.write(text)
