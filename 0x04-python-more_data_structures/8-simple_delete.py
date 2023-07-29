#!/usr/bin/python3

def simple_delete(a_dictionary, key):
    """Deletes a key in a dictionary.

    Args:
        a_dictionary (dict): The dictionary.
        key (str): The key to be deleted.

    Returns:
        The updated dictionary after deleting the key if it exists. If the key
        doesn't exist, the dictionary remains unchanged.

    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary

