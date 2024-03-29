#!/usr/bin/python3

"""contains the class definition of an ORM State"""

import sqlalchemy

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """ORM Representation of a state"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
