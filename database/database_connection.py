# -*- coding: utf-8 -*-

import sys
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import os

SQLALCHEMY_DATABASE_URI = None

if 'DATABASE_URI' in os.environ:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
else:
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://testuser:testpassword@localhost:5432/postgres"

Base = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(SQLALCHEMY_DATABASE_URI)


# Note order of events matters here
# we need to create the Base before importing User
from models.user_model import User
from models.transaction_model import Transaction

# def bind_engine():
engine = db_connect()  # Connect to database
Base.metadata.create_all(engine)  # Create models
