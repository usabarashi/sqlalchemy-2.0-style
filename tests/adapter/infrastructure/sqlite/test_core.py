from sqlalchemy import select

from adapter.infrastructure import sqlite
from adapter.infrastructure.sqlite import core


def test_insert():
    raise NotImplementedError


def test_update():
    raise NotImplementedError


def test_select_one():
    raise NotImplementedError


def test_select_all():
    statement = select([core.user.c.id, core.user.c.name, core.user.c.email_address])
    [result, *_] = sqlite.engine.execute(statement)
    assert "john doe" == result.name
    assert "example@example.com" == result.email_address


def test_select_delete():
    raise NotImplementedError
