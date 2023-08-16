#!/usr/bin/python3
"""
This function writes Object to text file using JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to text a file using JSON representation
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
