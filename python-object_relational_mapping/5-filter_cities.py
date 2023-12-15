#!/usr/bin/python3

"""
Script that takes in the name of a state as an argument and lists all cities of that state
The script should take 4 arguments:
    --  mysql username
    --  mysql passwd
    --  database name
    --  state name
The MySQLdb module must be used
Results must be sorted in ASC ORDER BY cities.id
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
    query = "SELECT cities.name FROM cities INNER JOIN states ON\
            cities.state_id = states.id WHERE states.name = %s"

    # Execute the query
    cur.execute(query, (sys.argv[4],))

    # Fetch all the rows
    result_tuple = cur.fetchall()
    words = [each_tpl[0] for each_tpl in result_tuple]
    result_string = ', '.join(words)
    print(result_string)
        
    # Close the cursos and the connection
    cur.close()
    db.close()
