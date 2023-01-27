#!/usr/bin/python3
"""
    Function that prints the name of a person
"""


def say_my_name(first_name, last_name=""):
    """
    Args:
        first_name: string
        last_name: string
    Raises:
        TypeError:
                 * first_name must be a string
                 * last_name must be a string
    Returns:
        print the name and last name
    """
    if first_name is None or type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if last_name is None or type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))
