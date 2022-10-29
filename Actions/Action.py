from abc import ABC, abstractmethod
from sre_parse import State


class Action(ABC):

    def __init__(self) -> None:
        return

    @abstractmethod
    def apply(self, state):
        pass