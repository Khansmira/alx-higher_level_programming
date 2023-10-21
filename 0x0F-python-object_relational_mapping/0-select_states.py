#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
from sys import argv

def main():
    """Lists states from hbtn_0e_0_usa
    """
    MY_HOST = 'localhost'
    MY_PORT = 3306
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    
    """Connect to the MySQL database
    """
    db = MySQLdb.connect(host=MY_HOST, port=MY_PORT, user=MY_USER, passwd=MY_PASS, db=MY_DB)
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

if __name__ == "__main__":
        main()
