#!/usr/bin/python3

"""
list all 'states' from the hbtn_0e_0_usa DB this script should take 3 arguments:
    -- ysql username
    -- mysql password
    -- database name (no argument validation needed)
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
    # Execute the query
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    # Fetch all the rows
    rows = cur.fetchall()
    for row in rows:
        city_name = row[1]
        if city_name[0] == "N":
            print(row)
    # Close the cursos and the connection
    cur.close()
    db.close()
