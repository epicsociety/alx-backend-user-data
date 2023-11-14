#!/usr/bin/env python3
"""SQLAlchemy model
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    """ class to which users table is mapped"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __repr__(self):
        """ Format the User object"""
        return ("<User(id={}, email={}, hashed_password={}, session_id={}, reset_token={})>"  # noqa: E501
                .format(self.id, self.email, self.hashed_password,
                        self.session_id, self.reset_token))
