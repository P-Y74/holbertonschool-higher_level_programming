#!/usr/bin/python3
"""
List all states with a name starting with 'N' from the database.

This script connects to a MySQL database and retrieves all rows
from the 'states' table where the name starts with 'N',
sorted by ID in ascending order.

Usage:
    ./0-select_states.py <username> <password> <database>

Arguments:
    username (str): MySQL username
    password (str): MySQL password
    database (str): Name of the MySQL database to query
"""


import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn.close()
