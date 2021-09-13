from sqlalchemy import select
from adapter.infrastructure import sqlite
from adapter.infrastructure.sqlite.declarative_table import UserDBModel


def test_insert():
    raise NotImplementedError


def test_update():
    raise NotImplementedError


def test_select_one():
    result = sqlite.engine.execute(select(UserDBModel)).fetchone()
    assert "john doe" == result.name
    assert "example@example.com" == result.email_address


def test_select_all():
    [result, *_] = sqlite.engine.execute(select(UserDBModel)).fetchall()
    assert "john doe" == result.name
    assert "example@example.com" == result.email_address


def test_delete():
    raise NotImplementedError
