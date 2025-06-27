#!/usr/bin/python3
"""
This script deletes all State objects with a name containing the letter 'a'
from the database `hbtn_0e_6_usa`.

Usage:
    ./script.py <mysql_username> <mysql_password> <database_name>

The script:
- Connects to a MySQL server on localhost using provided credentials.
- Deletes all entries in the `states` table whose name contains 'a'.
- Commits the changes.
- Does not execute if imported as a module.

Requirements:
- SQLAlchemy must be installed.
- The `State` and `Base` classes must be imported from `model_state`.
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

    session.query(State).filter(State.name.like(
        '%a%')).delete(synchronize_session=False)  # type: ignore
    session.commit()

    session.close()
