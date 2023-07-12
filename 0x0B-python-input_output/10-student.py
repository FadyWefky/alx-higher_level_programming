#!/usr/bin/python3
"""Student that defines a student"""


class Student():
    """class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """that retrieves a dictionary representation of a Student"""
        dictionary = self.__dict__
        new_dict = {}
        if attrs is None:
            return self.__dict__
        for key in attrs:
            if type(key) is not str:
                return self.__dict__
            else:
                if key in dictionary:
                    new_dict[key] = dictionary[key]
        return new_dict

    def reload_from_json(self, json):
        """Reload"""
        for key, data in json.items():
            self.__dict__[key] = data
