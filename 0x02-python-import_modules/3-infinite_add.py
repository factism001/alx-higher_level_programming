#!/usr/bin/python3
if __name__  "__main__":
    import sys

    sum = 0
    for i in sys.argv:
        if i != sys.argv[0]:
            sum += int(sum)
    print("{}".format(sum))
