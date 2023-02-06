#!/usr/bin/python3
"""
function that search if an attribute exist or not
"""


def add_attribute(obj, attr, value):
    if not hasattr(obj, "__dict__"):
        raise TypeError('can\'t add new attribute')
    else:
        setattr(obj, attr, value)
