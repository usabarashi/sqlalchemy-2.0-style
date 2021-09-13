from sqlalchemy import Column, Integer, String

from adapter.infrastructure import sqlite


@sqlite.mapper_registry.mapped
class UserDBModel:
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email_adddress = Column(String)