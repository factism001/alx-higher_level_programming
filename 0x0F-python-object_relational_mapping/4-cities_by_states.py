#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main":
    db = db.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, state.name FROM cities \
                JOIN states ON cities.state.id = state.id \
                ORDER BY cities.id")
    [print(cities) for cities in cur.fetchall()]
