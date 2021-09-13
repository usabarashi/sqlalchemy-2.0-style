from __future__ import annotations
from dataclasses import dataclass, replace


@dataclass(frozen=True)
class User:
    id_: int  # type: ignore
    name: str
    email_address: str

    def modify(self, name: str, email_address: str) -> User:
        return replace(self, name=name, email_address=email_address)
