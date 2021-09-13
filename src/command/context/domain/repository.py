from abc import ABC, abstractmethod
from typing import Any, Optional
from dataclasses import dataclass

from command.context.domain import user


@dataclass(frozen=True)
class Repository(ABC):
    """Repository"""

    session: Any  # FIXME

    @staticmethod
    def create(name: str, email_address: str) -> user.User:
        """新規作成

        - 未永続化のEntityはidが未採番のため, Noneで仮置する
        """
        return user.User(
            id_=None,  # type: ignore
            name=name,
            email_address=email_address,
        )

    @abstractmethod
    def get(self, id_: int) -> Optional[user.User]:
        """取得

        - idに該当するEntityを返却する
        - idに害するとEntityが存在しない場合はNoneを返却する
        """
        raise NotImplementedError

    @abstractmethod
    def save(self, entity: user.User) -> user.User:
        """永続化

        - 登録の場合, idを採用したEntityを返却する
        - 更新の場合, 更新結果のEntityを返却する
        """
        raise NotImplementedError
