#!/usr/bin/python3
"""
This function returns JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """
    returns JSON representation of an object (string)
    """
    return json.dumps(my_obj)
