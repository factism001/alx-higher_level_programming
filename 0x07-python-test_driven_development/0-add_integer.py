#!/usr/bin/python3
"""
   Function that return the addition of two numbers
"""


def add_integer(a, b=98):
    """
    Args:
         a: integer or float
         b: integer or float
    Raises:
         TypeError: a must be an integer
         TypeError: b must be an integer
    Returns:
         Addition of two numbers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return(a + b)
