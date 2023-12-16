#!/usr/bin/python3

"""This script lists all State objects from hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":

    session_crdt = "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(session_crdt, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    """Extract a sessioni"""

    States = session.query(State).all()

    for state in States:
        print("{}: {}".format(state.id, state.name))
