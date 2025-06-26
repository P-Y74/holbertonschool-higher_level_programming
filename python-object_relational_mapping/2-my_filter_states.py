#!/usr/bin/python3
"""
List all states with a name starting with a given letter from the database.

This script connects to a MySQL database and retrieves all rows
from the 'states' table where the name starts with the provided input string,
sorted by ID in ascending order.

Usage:
    ./0-select_states.py <username> <password> <database> <state_name_start>

Args:
    username (str): MySQL username.
    password (str): MySQL password.
    database (str): Name of the MySQL database to query.
    state_name_start (str): The starting string of the state name to filter by.

Raises:
    MySQLdb.OperationalError: If connection to the MySQL server fails.
"""


import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    input = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(input))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn.close()
