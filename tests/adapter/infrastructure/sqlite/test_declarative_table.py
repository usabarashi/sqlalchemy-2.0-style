from sqlalchemy import select, sql

from adapter.infrastructure import sqlite
from adapter.infrastructure.repository import declarative_table_repository
from adapter.infrastructure.sqlite.declarative_table import User

repository = declarative_table_repository.Repository(session=sqlite.session)


def test_Entity登録():
    """Entity登録

    idが採番されること
    """
    repository.session.begin()
    try:
        entity = repository.create(
            name="John Doe", email_address="john.doe@example.com"
        )
        saved_entity = repository.save(entity)
        assert id(entity) != id(saved_entity)
        assert None is not saved_entity.id_
        assert "John Doe" == saved_entity.name
        assert "john.doe@example.com" == saved_entity.email_address
        repository.session.commit()
    except Exception:
        repository.session.rollback()
        raise


def test_Entity更新():
    """Entity更新"""

    repository.session.begin()
    try:
        entity = repository.create(
            name="John Doe", email_address="john.doe@example.com"
        )
        saved_entity = repository.save(entity)
        modify_entity = saved_entity.modify(
            name="Jane Doe", email_address="jane.doe@example.com"
        )
        modified_entity = repository.save(entity=modify_entity)
        assert id(modify_entity) != id(modified_entity)
        assert saved_entity.id_ == modified_entity.id_
        assert "Jane Doe" == modified_entity.name
        assert "jane.doe@example.com" == modified_entity.email_address
        sqlite.session.commit()
    except Exception:
        sqlite.session.rollback()
        raise


def test_Entity取得():
    """Entity取得

    idに該当するEntityが存在しない場合はNoneを返却すること
    """
    repository.session.begin()
    try:
        entity = repository.get(id_=1)
        if entity is None:
            assert None is not entity
        else:
            assert 1 == entity.id_
            assert "John Doe" == entity.name
            assert "john.doe@example.com" == entity.email_address
        repository.session.commit()
    except Exception:
        repository.session.rollback()
        raise


def test_レコード取得():
    """レコード取得

    Repository経由で取得しないこと
    """
    sqlite.session.begin()
    try:
        statement = select(User).where(User.name == "John Doe")
        [result, *_] = sqlite.session.execute(statement).scalars().all()
        assert None is not result.id
        assert "John Doe" == result.name
        assert "john.doe@example.com" == result.email_address
        sqlite.session.commit()
    except Exception:
        sqlite.session.rollback()
        raise


def test_レコード削除():
    """レコード削除

    Repository経由で削除しないこと
    """
    sqlite.session.begin()
    try:
        entity = repository.create(
            name="John Doe", email_address="john.doe@example.com"
        )
        saved_entity = repository.save(entity)
        statement = select(User).where(User.id == saved_entity.id_)
        delete_entity = sqlite.session.execute(statement).scalars().first()
        sqlite.session.delete(delete_entity)
        sqlite.session.flush()
        maybe_entity = repository.get(id_=saved_entity.id_)
        assert None is not maybe_entity
        sqlite.session.commit()
    except Exception:
        sqlite.session.rollback()
        raise
