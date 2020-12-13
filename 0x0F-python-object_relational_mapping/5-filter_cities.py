#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists
    all cities of that state, using the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    serv = MySQLdb.connect(host="localhost",  port=3306,
                           user=sys.argv[1], password=sys.argv[2],
                           database=sys.argv[3])

    c = serv.cursor()
    stateName = sys.argv[4]
    c.execute("SELECT  cities.name FROM cities\
               JOIN states ON cities.state_id = states.id\
               ORDER BY cities.id ASC")
    rows = c.fetchall()
    for row in rows:
        if row[2] == stateName:
            print(','.join(row), end=" ", sep=" ")
    print()
    c.close()
    serv.close()
