from sqlalchemy import Column, Integer, String
from sqlalchemy.schema import Table

from adapter.infrastructure import sqlite


class UserDBModel(sqlite.Base):
    __tablename__ = Table(
        "user",
        sqlite.Base.metadata,
        Column("id", Integer, primary_key=True),
        Column("name", String),
        Column("email_address", String),
    )
