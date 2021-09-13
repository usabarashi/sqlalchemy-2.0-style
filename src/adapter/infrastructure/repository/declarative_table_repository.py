from dataclasses import asdict, dataclass
from typing import Optional

from sqlalchemy import update, select
from sqlalchemy.orm import Session

from adapter.infrastructure.sqlite import declarative_table
from command.context.domain import user, repository


@dataclass(frozen=True)
class Repository(repository.Repository):
    """Repository"""

    session: Session

    def get(self, id_: int) -> Optional[user.User]:
        """取得

        - idに該当するEntityを返却する
        - idに害するとEntityが存在しない場合はNoneを返却する
        """
        statement = select(declarative_table.User)
        result = self.session.execute(statement).scalars().first()
        if result is None:
            return None
        else:
            return user.User(
                id_=result.id, name=result.name, email_address=result.email_address
            )

    def save(self, entity: user.User) -> user.User:
        """永続化

        - 登録の場合, idを採番したEntityを返却する
        - 更新の場合, 更新結果のEntityを返却する
        """
        # Insert
        if entity.id_ is None:
            insert_entity = declarative_table.User(
                name=entity.name, email_address=entity.email_address
            )
            self.session.add(insert_entity)
            self.session.flush()
            return user.User(
                id_=insert_entity.id,
                name=insert_entity.name,
                email_address=insert_entity.email_address,
            )
        # Update
        else:
            statement = (
                update(declarative_table.User)
                .where(id == entity.id_)
                .values(name=entity.name, email_address=entity.email_address)
            )
            self.session.execute(statement)
            return user.User(**asdict(entity))
