#!/usr/bin/python3
"""
Retrieves the ID of a State object with a given name from a MySQL database.

This script connects to a MySQL database using SQLAlchemy and queries for
a State object whose name matches the value passed as the fourth command-line
argument. If found, it prints the state's ID. Otherwise, it prints "Not found".

Usage:
    ./script.py <mysql_username> <mysql_password> <database_name> <state_name>

Args:
    mysql_username (str): MySQL username.
    mysql_password (str): MySQL password.
    database_name (str): Name of the MySQL database to connect to.
    state_name (str): Name of the state to search for.

Example:
    ./script.py root root hbtn_0e_6_usa Texas

Note:
    - The script uses SQLAlchemy's ORM to prevent SQL injection.
    - Results are case-sensitive.
"""
import sys

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)  # type: ignore

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(
        State.name == sys.argv[4]).first()  # type: ignore

    if states:
        print(f"{states.id}")
    else:
        print("Not found")

    session.close()
