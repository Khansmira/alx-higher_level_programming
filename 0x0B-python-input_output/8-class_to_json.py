#!/usr/bin/python3
"""
This function returns the Dictionary description with simple data
structure for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Returns the dictionary description with
    simple data structure (list, dictionary,
    string, integer and boolean) for JSON
    serialization of an object
    """
    return (obj.__dict__)
