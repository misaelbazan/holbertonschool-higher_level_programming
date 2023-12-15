#!/usr/bin/python3


"""script that lists all cities from hbtn_0d_4_usa:
    --  the script should take 3 arguments:
        mysql username, mysql passwd database
    --  the MySQLdb module must be used (import MySQLdb)
    --  the script should connect toa MySQL server running on:
        host:'localhost'
        port:3306
    --  results must be sorted in ARC ORDER BY cities.id
    --  execute() can only be used once
    --  the code should not be executed when imported

"""


import sys
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8"
            )
    cur = conn.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities\
            LEFT JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id"
    cur.execute(query)
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
