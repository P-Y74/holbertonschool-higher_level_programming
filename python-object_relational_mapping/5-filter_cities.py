#!/usr/bin/python3
"""
5-filter_cities.py

This script lists all cities of a given state from the database
`hbtn_0e_4_usa`.

It connects to a MySQL server running on `localhost` at port `3306`,
performs a secure SQL query using parameter substitution
(to prevent SQL injection),
and prints all city names belonging to the specified state, sorted by city ID.

Usage:
    ./5-filter_cities.py <mysql_username> <mysql_password> <database_name>
    <state_name>

Example:
    ./5-filter_cities.py root root hbtn_0e_4_usa Texas

Args:
    mysql_username (str): MySQL server username.
    mysql_password (str): MySQL server password.
    database_name (str): Name of the MySQL database.
    state_name (str): Name of the state to search cities for (case-sensitive).

Requirements:
    - MySQL server must be running locally on port 3306.
    - The `MySQLdb` module must be installed (`pip install mysqlclient`).

Author:
    Your Name
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

    cursor.execute("SELECT cities.id, cities.name, states.name "
                   "FROM cities "
                   "JOIN states ON cities.state_id = states.id "
                   "WHERE BINARY states.name = %s "
                   "ORDER BY cities.id ASC", (state_name,))
    rows = cursor.fetchall()
    print(", ".join(row[1] for row in rows))

    cursor.close()
    conn.close()
