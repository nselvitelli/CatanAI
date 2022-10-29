from abc import ABC, abstractmethod


class Action(ABC):

    def __init__(self) -> None:
        return

    @abstractmethod
    def apply(self, state):
        pass