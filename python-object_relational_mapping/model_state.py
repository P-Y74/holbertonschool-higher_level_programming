#!/usr/bin/python3
"""
This module defines a `State` class that represents a row in the `states`
table.

It uses SQLAlchemy's Object Relational Mapping (ORM) to map the class
to a MySQL table. This class inherits from the SQLAlchemy declarative base.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """
    A class that represents a state in the MySQL database.

    Attributes:
        __tablename__ (str): Name of the table in the database.
        id (int): Primary key, auto-incremented, cannot be null.
        name (str): Name of the state, string up to 128 characters,
        cannot be null.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
