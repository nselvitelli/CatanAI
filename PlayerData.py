from enum import Enum

from Resource import Resource


class PlayerData:

    def __init__(self) -> None:
        self.resourcesAvailable = {}
        self.resourcesAvailable[Resource.WHEAT] = 0
        self.resourcesAvailable[Resource.BRICK] = 0
        self.resourcesAvailable[Resource.LOG] = 0
        self.resourcesAvailable[Resource.ORE] = 0
        self.resourcesAvailable[Resource.SHEEP] = 0




class PlayerColor(Enum):
    WHITE = 0
    RED = 1
    BLUE = 2
    ORANGE = 3
    BLANK = 4
