#!/usr/bin/python3
"""
Filter states by name from the database in a secure way.

This script connects to a MySQL database and retrieves all rows from the
'states' table where the name matches a given argument. The query is
parameterized to prevent SQL injection attacks. Results are sorted by ID
in ascending order.

Usage:
    ./2-my_filter_states.py <username> <password> <database> <state_name>

Args:
    username (str): MySQL username.
    password (str): MySQL password.
    database (str): Name of the MySQL database to connect to.
    state_name (str): The name of the state to search for (case-sensitive).

Example:
    ./2-my_filter_states.py root root hbtn_0e_0_usa Nevada

Raises:
    MySQLdb.OperationalError: If the connection to the MySQL server fails.
    IndexError: If not enough arguments are provided.
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

    cursor.execute("SELECT * FROM states WHERE BINARY name = %s"
                   "ORDER BY id ASC", (state_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn.close()
