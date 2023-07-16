#!/usr/bin/python3
# base.py
"""
first class Base file
"""
import json
import os
import os.path
import csv
import random


class Base():
    """first class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """json to string"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save to file"""
        filename = cls.__name__ + ".json"
        with open(filename, mode='w') as jsonf:
            if list_objs is None:
                jsonf.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonf.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance from a dictionary"""
        if (cls.__name__ == "Square"):
            dummy = cls(2)
        elif (cls.__name__ == "Rectangle"):
            dummy = cls(2, 2)
        dummy.update(**dictionary)
        return(dummy)

    @classmethod
    def load_from_file(cls):
        """Loads file and returns a list of instances"""
        instance_list = []
        filename = cls.__name__ + ".json"
        if not os.path.isfile(filename):
            return (instance_list)
        with open(filename) as my_file:
            my_data = cls.from_json_string(my_file.read())
            for instance in my_data:
                instance_list.append(cls.create(**instance))
        return (instance_list)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file"""
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
        """Return a list of classes instantiated from a CSV file"""
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
