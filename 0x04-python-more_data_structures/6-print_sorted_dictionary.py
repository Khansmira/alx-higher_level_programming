#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys.

    Args:
        a_dictionary (dict): The dictionary to be printed.

    """
    # Get the keys of the dictionary in sorted order
    sorted_keys = sorted(a_dictionary.keys())

    # Iterate through the sorted keys and print each key-value pair
    for key in sorted_keys:
        # Use the format method to print the key and its corresponding value
        print('{}: {}'.format(key, a_dictionary[key]))
