#!/usr/bin/python3
"""
This function returns  an py data structure object respresented by JSON string
"""
import json


def from_json_string(my_str):
    """
    Returns object represented by JSON string
    """
    return json.loads(my_str)
