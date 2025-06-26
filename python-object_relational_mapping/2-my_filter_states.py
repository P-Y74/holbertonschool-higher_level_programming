#!/usr/bin/python3
"""
Display all states from the database where the name matches the given argument.

This script connects to a MySQL database and retrieves all rows
from the 'states' table where the name matches exactly the provided state name.
Results are sorted by state ID in ascending order.

Usage:
    ./script.py <username> <password> <database> <state_name>

Args:
    username (str): MySQL username.
    password (str): MySQL password.
    database (str): Name of the MySQL database to query.
    state_name (str): State name to search for.

Raises:
    MySQLdb.OperationalError: If the connection to the MySQL server fails.
"""


import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM states WHERE BINARY name LIKE '{}%'"
                   "ORDER BY id ASC".format(state_name))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn.close()
