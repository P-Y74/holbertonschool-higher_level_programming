#!/usr/bin/python3
"""
Lists all State objects from the database using SQLAlchemy.

This script connects to a MySQL database using credentials provided via
command-line arguments, queries all records from the `states` table,
and prints them sorted by `id`.

Usage:
    ./6-model_state.py <mysql_username> <mysql_password> <database_name>

Args:
    mysql_username (str): The MySQL username.
    mysql_password (str): The MySQL password.
    database_name (str): The name of the MySQL database.

Example:
    ./6-model_state.py root root hbtn_0e_6_usa

Note:
    This script uses SQLAlchemy ORM and requires `model_state.py` to define
    the `Base` and `State` classes.
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
    Base.metadata.create_all(engine) # type: ignore

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all() # type: ignore
    
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
