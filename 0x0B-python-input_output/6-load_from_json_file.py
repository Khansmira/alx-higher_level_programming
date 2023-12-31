#!/usr/bin/python3
"""
This function creates an Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    Creates a Py object from a 'JSON file'
    """
    with open(filename, "r", encoding='utf-8') as f:
        return json.load(f)
