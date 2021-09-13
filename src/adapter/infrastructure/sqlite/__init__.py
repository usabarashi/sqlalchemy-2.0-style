# see: https://docs.sqlalchemy.org/en/14/changelog/migration_20.html#migration-orm-configuration
from sqlalchemy import column, create_engine, select, table
from sqlalchemy.orm import declarative_base, registry

DB_URL = "sqlite:///test.db"
engine = create_engine(DB_URL)
Base = declarative_base()
mapper_registry = registry()

CREATE_TABLE = """
    CREATE TABLE user (
        id integer PRIMARY KEY AUTOINCREMENT,
        name nvarchar NOT NULL,
        email_address nvarchar NOT NULL
    )
    """
INSERT_RECORD = """
    INSERT INTO user (
        name,
        email_address
    ) VALUES (
        'john doe',
        'example@example.com'
    )
    """

# engine.execute(CREATE_TABLE)
# engine.execute(INSERT_RECORD)

user = table("user", column("id"), column("name"), column("email_address"))
result = engine.execute(select([user.c.id, user.c.name, user.c.email_address]))

print(result.fetchall())
