#!/usr/bin/python3
"""
This module contains the Base for other classes in this project
"""


import json
import os
import csv


class Base:
    """
    A representation of the Base for other classes in this project
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        class Constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON representation to a file
        """
        file_name = cls.__name__ + ".json"
        with open(file_name, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_objs = [o.to_dictionary() for o in list_objs]
                f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation
        """
        string_list = []
        if json_string is None:
            return string_list
        else:
            string_list = json.loads(json_string)
            return string_list

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all the attributes already set in the dictionary
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns list of instances
        """

        file_name = cls.__name__ + ".json"
        if os.path.exists(file_name):
            with open(file_name, 'r', encoding="utf-8") as f:
                _string = f.read()
                list_dictionaries = cls.from_json_string(_string)
                for dictionary in list_dictionaries:
                    list_instances.append(cls.create(**dictionary))
        return list_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes list_objs and saves them to a csv file
        """
        file_name = cls.__name__ + ".csv"
        with open(file_name, "w", newline="", encoding="utf-8") as f_csv:
            if list_objs is None or list_objs == []:
                f_csv.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f_csv, fieldnames=fieldnames)
                for objs in list_objs:
                    writer.writerow(objs.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes the CSV format and loads object from a csv file
        """
        filename = cls.__name__ + ".csv"
        instances = []

    try:
        with open(filename, "r", newline="", encoding="utf-8") as f_csv:
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            else:
                fieldnames = ["id", "size", "x", "y"]
            
            reader = csv.DictReader(f_csv, fieldnames=fieldnames)
            
            for row in reader:
                d = {k: int(v) for k, v in row.items()}
                instance = cls.create(**d)
                instances.append(instance)

    except FileNotFoundError:
        pass

    return instances
