from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    id_: int
    name: str
    email_address: str

    def __new__(cls):
        pass
