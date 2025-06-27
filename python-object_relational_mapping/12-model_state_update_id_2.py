#!/usr/bin/python3
"""
Change the name of the State object with id = 2 to "New Mexico" in the
database.

This script connects to a MySQL database using SQLAlchemy, updates the state
with id 2 to have the name "New Mexico", and commits the change.

Usage:
    ./script.py <mysql_username> <mysql_password> <database_name>

Arguments:
    mysql_username (str): Username for the MySQL database.
    mysql_password (str): Password for the MySQL database.
    database_name (str): Name of the MySQL database.

Notes:
    - The script connects to a MySQL server running on localhost at port 3306.
    - Requires the State and Base classes from model_state.py.
    - The code does not execute if imported as a module.
"""
import sys

from model_state import Base, State
from sqlalchemy import create_engine, update
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

    change_state = update(State).where(State.id == 2).values(
        name=('New Mexico'))
    session.execute(change_state)
    session.commit()

    session.close()
