#!/usr/bin/python3
"""
Adds a new State object "Louisiana" to the database and prints its id.

Connects to a MySQL database using SQLAlchemy with credentials and
database name provided as command line arguments.

Usage:
    ./script.py <mysql_username> <mysql_password> <database_name>

Prints:
    The id of the newly created State object "Louisiana".

Note:
    The script must be run with exactly three arguments.
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

    new_state = State(name="Louisiana")  # type: ignore
    session.add(new_state)
    session.commit()

    states = session.query(State).order_by(State.id).all()  # type: ignore

    print(f"{new_state.id}")

    session.close()
