#!/usr/bin/python3
def uniq_add(my_list=[]):
    i = 0
    if my_list is not None:
        unique_elements = set()
        for element in my_list:
            if element not in unique_elements:
                i = i + element
                unique_elements.add(element)
    return i
