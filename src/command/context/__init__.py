from abc import ABC, abstractmethod
from typing import Callable, TypeVar

T = TypeVar("T")


class Transaction(ABC):
    @abstractmethod
    def acid(self, trannsaction: Callable[..., T]) -> T:
        raise NotImplementedError
