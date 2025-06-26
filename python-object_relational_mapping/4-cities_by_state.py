#!/usr/bin/python3
"""
List all cities in the database hbtn_0e_4_usa with their corresponding states.

This script connects to a MySQL database and retrieves all rows from the
'cities' table, along with their associated state names from the 'states' table,
using an inner join. Results are sorted by cities.id in ascending order.

Usage:
    ./4-cities_by_state.py <username> <password> <database>

Args:
    username (str): MySQL username.
    password (str): MySQL password.
    database (str): Name of the MySQL database to connect to.

Example:
    ./4-cities_by_state.py root root hbtn_0e_4_usa

Raises:
    MySQLdb.OperationalError: If the connection to the database fails.
    IndexError: If not enough arguments are provided.
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

    cursor.execute("SELECT cities.id, cities.name, states.name "
                   "FROM cities "
                   "JOIN states ON cities.state_id = states.id "
                   "ORDER BY cities.id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn.close()
