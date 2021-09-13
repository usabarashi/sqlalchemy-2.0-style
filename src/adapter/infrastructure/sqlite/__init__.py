# see: https://docs.sqlalchemy.org/en/14/changelog/migration_20.html#migration-orm-configuration
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, registry, Session

DB_URL = "sqlite:///test.db"
engine = create_engine(DB_URL, future=True)
session = Session(engine)
Base = declarative_base()
mapper_registry = registry()

DROP_TABLE = """
    DROP TABLE IF EXISTS users; 
    """
CREATE_TABLE = """
    CREATE TABLE user (
        id integer PRIMARY KEY AUTOINCREMENT,
        name nvarchar NOT NULL,
        email_address nvarchar NOT NULL
    );
    """
# session.execute(DROP_TABLE)
# session.execute(CREATE_TABLE)
