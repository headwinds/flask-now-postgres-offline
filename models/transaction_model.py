# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON
from database.database_connection import Base
import datetime


class Transaction(Base):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True)
    title = Column(String(30), unique=False)
    type = Column(String(30), unique=False)
    cost = Column(Integer)
    transaction_json = Column(JSON)
    user_id = Column(
        Integer,
        ForeignKey('user.id', ondelete='CASCADE'),
        nullable=False,
        # no need to add index=True, all FKs have indexes
    )
    user = relationship('User', backref='transactions')
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, onupdate=datetime.datetime.now)

    def __repr__(self):
        return '<Transaction %r>' % self.title
