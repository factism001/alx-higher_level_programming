#!/usr/bin/python3
"""Module that contains class named Base"""


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=none):
        """initializes the instances"""
        if id != none:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
