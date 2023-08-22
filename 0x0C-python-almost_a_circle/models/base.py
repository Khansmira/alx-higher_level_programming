#!/usr/bin/python3
"""This serves as the base for other classes"""


import csv
import json
import os
import turtle


class Base:
    """Represents the base of all the classes created """

    __nb_objects = 0

    def __init__(self, id=None):
        """ """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or not
                all(type(i) == dict for i in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save the JSON representation to file"""
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of JSON string representations"""
        json_string_list = []

        if json_string is not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            json_string_list = json.loads(json_string)

        return json_string_list

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all the attributes already set"""
        # create an instance of an existing class
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns list of instances"""

        file_name = cls.__name__ + ".json"
        list_of_instances = []
        list_dictionaries = []

        if os.path.exists(file_name):
            with open(file_name, 'r') as my_file:
                my_str = my_file.read()
                list_dictionaries = cls.from_json_string(my_str)
                for dictionary in list_dictionaries:
                    list_of_instances.append(cls.create(**dictionary))
        return list_of_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs and saves them to file"""

        # if (type(list_objs) != list and list_objs is not None
        #    or not all(isinstance(i, cls) for i in list_objs)):

        #     raise TypeError("list_objs must be a list of instances")

        # file_name = cls.__name__ + ".csv"
        # with open(file_name, 'w') as my_file:
        #     if list_objs is not None:
        #         list_objs = [i.todictionary for i in list_objs]
        #         if cls.__name__ == 'Rectangle':
        #             records = ['id', 'width', 'height', 'x', 'y']
        #         elif cls.__name__ == 'Square':
        #             records = ['id', 'size', 'x', 'y']
        #         script = csv.DictWriter(my_file, fieldnames=records)
        #         script.writeheader()
        #         script.writerows(list_objs)

        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes the CSV format from a file"""

        # file_name = cls.__name__ + ".csv"
        # list_of_instances = []
        # if os.path.exists(file_name):
        #     with open(file_name, 'r') as my_file:
        #         reader = csv.reader(my_file, delimiter=',')
        #         if cls.__name__ == 'Rectangle':
        #             records = ['id', 'width', 'height', 'x', 'y']
        #         elif cls.__name__ == 'Square':
        #             records = ['id', 'size', 'x', 'y']
        #         for i, row in enumerate(reader):
        #             if i > 0:
        #                 x = cls(1, 1)
        #                 for j, y in enumerate(row):
        #                     if y:
        #                         setattr(x, records[j], int(y))
        #                 list_of_instances.append(x)
        # return list_of_instances

        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        trtl = turtle.Turtle()
        trtl.screen.bgcolor("#b7312c")
        trtl.pensize(3)
        trtl.shape("turtle")

        trtl.color("#ffffff")
        for rect in list_rectangles:
            trtl.showturtle()
            trtl.up()
            trtl.goto(rect.x, rect.y)
            trtl.down()
            for i in range(2):
                trtl.forward(rect.width)
                trtl.left(90)
                trtl.forward(rect.height)
                trtl.left(90)
            trtl.hideturtle()

        trtl.color("#b5e3d8")
        for sq in list_squares:
            trtl.showturtle()
            trtl.up()
            trtl.goto(sq.x, sq.y)
            trtl.down()
            for i in range(2):
                trtl.forward(sq.width)
                trtl.left(90)
                trtl.forward(sq.height)
                trtl.left(90)
            trtl.hideturtle()

        turtle.exitonclick()
