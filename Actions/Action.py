from abc import ABC, abstractmethod
from enum import Enum
from sre_parse import State


class Action(ABC):

    def __init__(self, debug) -> None:
        self.debug = debug

    @abstractmethod
    def apply(self, state):
        pass

    @abstractmethod
    def getActionAsString(self):
        pass

class EAction(Enum):
    DISCARD = 0
    NEXTPLAYER = 1
    MOVEROBBER = 2
    ROLLDICE = 3
    PLACE_INIT_SETTLEMENT = 4
    PLACE_INIT_SETTLEMENT_GET_RESOURCES = 5
    BUILDFREEROAD = 6