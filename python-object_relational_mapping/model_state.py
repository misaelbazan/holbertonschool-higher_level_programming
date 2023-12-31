#!/usr/bin/python3

"""This module contains State class that inherits from Base"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Creating a class that inherits from Base"""

    __tablename__ = 'states'

    """Declaring class attributes"""
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
