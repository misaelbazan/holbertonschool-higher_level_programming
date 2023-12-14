#!/usr/bin/python3

"""
list all 'states' from the bhbtn_d_usa DB this script should take 3 arguments:
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


username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

# Establish a connection
db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
        )
cur = db.cursor()
# Execute the query
cur.execute("SELECT * FROM states ORDER BY states.id")
# Fetch all the rows
rows = cur.fetchall()
for row in rows:
    print(row)
# Close the cursos and the connection
cur.close()
db.close()

if __name__ == "__main__":
    pass
