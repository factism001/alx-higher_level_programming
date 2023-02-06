#!/usr/bin/python3
"""
class BaseGeometry
"""


class BaseGeometry:
    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')


class Rectangle(BaseGeometry):
    """
    class Rectangle as inheritance of class BaseGeometry
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return(self.__width * self.__height)

    def __str__(self):
        str1 = "[Rectangle] " + str(self.__width)
        str1 = str1 + "/" + str(self.__height)
        return (str1)
