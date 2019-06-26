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


def transaction_valid(title, type, cost, transaction_json):
    with session_scope() as s:
        """
        how do we prevent duplicate transactions?

        transaction = s.query(database_connection.Transaction).filter(
            database_connection.Transaction.id.in_([id])).first()

        if transaction:
            print("transaction_valid transaction success")
            print("transaction_valid transaction.id:", transaction.id)
            return False
        else:
            print("transaction_valid user fail")
            return False
        """
        return True


def add_transaction(title, type, cost, transaction_json):
    with session_scope() as s:
        # hashed_pw = hash_password(password)
        print("add_transaction transaction_json: ", transaction_json)
        u = database_connection.Transaction(
            user_id=1,
            title=title,
            type=type,
            cost=cost,
            transaction_json=transaction_json)
        s.add(u)
        s.commit()
        return True
    return False
