#!/usr/bin/python3

"""
Display all ocurrences values wherethe states name matches the sys.argv[4]
- This script should take 4 arguments:
    -- ysql username
    -- mysql password
    -- database name (no argument validation needed)
    -- state name searched
you must use the Module 'MySQLdb' (import)
the script should connect to a MySQL server running on localhost
at port '3306'
Results must be sorted in ASC order by states.id
The code should not be executed when imported
"""


import sys
import MySQLdb

# Establish a connection
if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8"
        )
    cur = db.cursor()
    # Describe the query
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"

    # Execute the query
    cur.execute(query, (sys.argv[4],))

    # Fetch all the rows
    rows = cur.fetchall()
    for row in rows:
        print(row)
    # Close the cursos and the connection
    cur.close()
    db.close()
