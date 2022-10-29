from enum import Enum

from Resource import Resource


class PlayerData:

    def __init__(self, wheat=0, brick=0, log=0, ore=0, sheep=0, devCards=[]) -> None:
        self.resourcesAvailable = {}
        self.resourcesAvailable[Resource.WHEAT] = wheat
        self.resourcesAvailable[Resource.BRICK] = brick
        self.resourcesAvailable[Resource.LOG] = log
        self.resourcesAvailable[Resource.ORE] = ore
        self.resourcesAvailable[Resource.SHEEP] = sheep

        self.devCards = []
        for devCard in devCards:
            self.devCards.push(devCard)

class PlayerColor(Enum):
    WHITE = 0
    RED = 1
    BLUE = 2
    ORANGE = 3
    BLANK = 4
