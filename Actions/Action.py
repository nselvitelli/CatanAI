from abc import ABC, abstractmethod
from enum import Enum
from sre_parse import State


class Action(ABC):

    def __init__(self) -> None:
        return

    @abstractmethod
    def apply(self, state):
        pass

class EAction(Enum):
    DISCARD = 0
    NEXTPLAYER = 1
    MOVEROBBER = 2
    ROLLDICE = 3