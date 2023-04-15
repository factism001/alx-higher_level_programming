#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    db = db.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM state ORDER BY id where BINARY name = '{}'".format(sys.argv[4]))
    [print(state) for state in cur.fetchall()]