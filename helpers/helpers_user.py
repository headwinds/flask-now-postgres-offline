# -*- coding: utf-8 -*-

import database.database_connection as database_connection
from flask import session
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from types import SimpleNamespace
import bcrypt


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    s = get_session()
    s.expire_on_commit = False
    try:
        yield s
        s.commit()
    except:
        s.rollback()
        raise
    finally:
        s.close()


def get_session():
    return sessionmaker(bind=database_connection.engine)()


def get_user():
    username = session['username']
    with session_scope() as s:
        user = s.query(database_connection.User).filter(
            database_connection.User.username.in_([username])).first()
        if user is not None:
            return user
        else:
            default_user = {"username": "please log in"}
            dot_user = SimpleNamespace(**default_user)
            return dot_user


# password=password.decode('utf8') not needed
def add_user(username, password, email):
    with session_scope() as s:
        # hashed_pw = hash_password(password)
        print("saving password: ", password)
        u = database_connection.User(username=username,
                                     password=password,
                                     email=email)
        s.add(u)
        s.commit()
        return True
    return False


def add_user_purchase(item):
    with session_scope() as s:
        u = database_connection.User(username=username,
                                     password=password,
                                     email=email)
        u.purchases.append(database_connection.Purchase(item))
        s.add(u)
        s.commit()


def change_user(**kwargs):
    username = session['username']
    with session_scope() as s:
        user = s.query(database_connection.User).filter(
            database_connection.User.username.in_([username])).first()
        for arg, val in kwargs.items():
            if val != "":
                setattr(user, arg, val)
        s.commit()


# https://stackoverflow.com/questions/34548846/flask-bcrypt-valueerror-invalid-salt
# read the J Mulet reply about decoding and postgres
def hash_password(password):
    pwhash = bcrypt.hashpw(password.encode('utf8'),
                           bcrypt.gensalt())  # was just this line
    return pwhash.decode('utf8')  # decode the hash to prevent is encoded twice


def credentials_valid(username, password):
    with session_scope() as s:
        user = s.query(database_connection.User).filter(
            database_connection.User.username.in_([username])).first()
        print("credentials_valid user:", user)
        if user:
            print("credentials_valid user success")
            print("credentials_valid user.password:", user.password)
            return bcrypt.checkpw(password.encode('utf8'),
                                  user.password.encode('utf8'))
        else:
            print("credentials_valid user fail")
            return False


def username_taken(username):
    with session_scope() as s:
        return s.query(database_connection.User).filter(
            database_connection.User.username.in_([username])).first()
