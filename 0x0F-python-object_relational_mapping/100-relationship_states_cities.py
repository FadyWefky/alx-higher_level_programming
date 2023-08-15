#!/usr/bin/python3
"""
14-model_city_fetch_by_state.py
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def init_sess():
    """initializes session and engine for sqlalchemy DB instance"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    return (engine, session)


def create_all(db):
    pass


if __name__ == '__main__':
    create_all(init_sess())
