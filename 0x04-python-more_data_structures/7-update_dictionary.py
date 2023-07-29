def update_dictionary(a_dictionary, key, value):
    """Replaces or adds key/value in a dictionary.

    Args:
        a_dictionary (dict): The dictionary.
        key (str): The key.
        value: The value.

    Returns:
        The updated dictionary with the key/value pair.

    """
    a_dictionary[key] = value
    return a_dictionary

