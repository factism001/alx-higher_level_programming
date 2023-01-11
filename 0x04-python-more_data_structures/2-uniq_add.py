#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    set_res = set(my_list)
    for i in set_res:
        sum += i
        return sum
