#!/usr/bin/python3
"""method for student creation"""


class Student:
    """Student obj"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        if type(attrs) is list:
            for things in attrs:
                if type(things) is not str:
                    return self.__dict__
        else:
            return self.__dict__
        new_dictionary = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dictionary.update({key, value})
        return new_dictionary
