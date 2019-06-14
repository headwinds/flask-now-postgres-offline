# -*- coding: utf-8 -*-

import sys
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import os

# SQLALCHEMY_DATABASE_URI = 'sqlite:///accounts.db'

local_uri = 'postgresql+psycopg2://dbusername:dbpassword@dbhost:dbport/dbname'
remote_uri = 'postgresql+psycopg2://dbusername:dbpassword@dbhost:dbport/dbname'
SQLALCHEMY_DATABASE_URI = None
if 'DATABASE_URI' in os.environ:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URI']
else:
    SQLALCHEMY_DATABASE_URI = local_uri

Base = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(SQLALCHEMY_DATABASE_URI)


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True)
    password = Column(String(512))
    email = Column(String(50))

    def __repr__(self):
        return '<User %r>' % self.username


engine = db_connect()  # Connect to database
Base.metadata.create_all(engine)  # Create models
