#!/usr/bin/python3
""" This script lists all states from the database hbtn_0e_0_usa. """


import MySQLdb
from sys import argv

if __name__ == '__main__':

    db_connect = MySQLdb.connect(
            host='localhost',
            user=argv[1],
            port=3306,
            passwd=argv[2],
            db=argv[3])

    cur = db_connect.cursor()

    cur.execute('SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC')

    rows = cur.fetchall()

    for row in rows:
        print(row)
