#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
"""



from sys import argv
import MySQLdb

if __name__ == '__main__':

    """
    Connect to the database
    """
    db_connect = MySQLdb.connect(host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    cur = db_connect.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db_connect.close()
