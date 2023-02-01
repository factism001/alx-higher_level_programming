#!/usr/bin/python3
def magic_string(list=[]):
    list += [1]
    return(("BestSchool, " * (len(list) - 1)) + "BestSchool")
