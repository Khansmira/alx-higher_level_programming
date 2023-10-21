#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    
    """Connect to the MySQL database
    """
    db_connect = MySQLdb.connect(host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])
    cur = db.cursor()
    
    """Execute the SQL query to retrieve states in ascending order by states.id
    """
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    """Fetch and Display all the results
    """
    selected_rows = cur.fetchall()
    for row in selected_rows:
        print(row)

    """Close all cursors and databases
    """
    cur.close()
    db.close()
