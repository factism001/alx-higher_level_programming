#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main":
    db = db.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * from cities JOIN states \
                ON cities.state_id = states.id ORDER BY cities.id")
    [print(",".join([city[2] for city in cur.fetchall() if city[4] == sys.argv[4]]))]