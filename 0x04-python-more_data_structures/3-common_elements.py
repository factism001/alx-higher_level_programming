#!/usr/bin/python3
def common_elements(set_1, set_2):
    a = set(set_1)
    b = set(set_2)
    common_set = a & b
    return [i for i in common_set]
