#!/usr/bin/python3
"""
Defines class: Student
"""


class Student:

    def __init__(self, first_name, last_name, age):
        """
        Attributes of Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Public method that retrieves a dictionary representation of a
        Student instance
        """
        if (isinstance(attrs, list) and
                all(isinstance(x, str) for x in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__
