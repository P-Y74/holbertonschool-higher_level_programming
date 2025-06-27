#!/usr/bin/python3
"""
Lists all State objects from the database whose name starts with 'a'.

Connects to a MySQL database using SQLAlchemy ORM and retrieves all State
records where the name begins with the letter 'a'. Results are sorted
in ascending order by the state's ID.

Usage:
    ./script.py <mysql_username> <mysql_password> <database_name>

Args:
    mysql_username (str): MySQL username.
    mysql_password (str): MySQL password.
    database_name (str): Database name.

Example:
    ./script.py root root_password hbtn_0e_6_usa
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
        State.name.like('%a%')).order_by(State.id).all()  # type: ignore

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
