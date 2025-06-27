#!/usr/bin/python3
"""
Script to retrieve and print the first State object from the MySQL database.

This script connects to a MySQL server using SQLAlchemy and prints the
first `State` object based on ascending `id`. If the table is empty, it
prints 'Nothing'.

Args:
    mysql_username (str): The MySQL username (passed as argv[1])
    mysql_password (str): The MySQL password (passed as argv[2])
    database_name (str): The name of the MySQL database (passed as argv[3])

Example:
    ./0-select_first_state.py root root hbtn_0e_6_usa
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

    states = session.query(State).order_by(State.id).first()  # type: ignore

    if states:
        print(f"{states.id}: {states.name}")
    else:
        print('Nothing')

    session.close()
