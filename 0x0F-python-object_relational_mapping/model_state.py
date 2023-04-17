#!/usr/bin/python3
"""
Defines a state model that contain the class definition
 of a State and an instance Base = declarative_base()
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class City(Base):
    """
    inherits from Base Tips
    links to the MySQL table states
    class attribute id that represents a column
     of an auto-generated, unique integer, can't
      be null and is a primary key
    class attribute name that represents a column
     of a string with maximum 128 characters and
      can't be null
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
