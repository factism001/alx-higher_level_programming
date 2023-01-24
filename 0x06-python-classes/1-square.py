#!/usr/bin/python3
""" oop with python class """


class Square():
    """Class representing a square"""

    def __init__(self, size):
        """ initialize the class
        Args:
           size (int): size of the square
        """
        self.__size = size
