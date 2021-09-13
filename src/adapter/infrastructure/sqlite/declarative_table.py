from sqlalchemy import Column, Integer, String

from adapter.infrastructure import sqlite


class User(sqlite.Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email_address = Column(String)
