from enum import Enum

from Resource import Resource


class PlayerData:

    def __init__(self, victoryPoints, devCards, longestRoad, largestArmy, settlements, resources, color) -> None:
        self.victoryPoints = victoryPoints

        # Note: NOT a deep copy (don't think it needs to be, never edit devcards)
        self.devCards = []
        for devCard in devCards:
            self.devCards.push(devCard)

        self.longestRoad = longestRoad
        self.largestArmy = largestArmy

        self.settlements = []
        for settlement in settlements:
            self.settlements.push(settlement)

        self.resourcesAvailable = {}
        self.resourcesAvailable[Resource.WHEAT] = resources[Resource.WHEAT] if resources.has_key(
            Resource.WHEAT) else 0
        self.resourcesAvailable[Resource.BRICK] = resources[Resource.BRICK] if resources.has_key(
            Resource.BRICK) else 0
        self.resourcesAvailable[Resource.LOG] = resources[Resource.LOG] if resources.has_key(
            Resource.LOG) else 0
        self.resourcesAvailable[Resource.ORE] = resources[Resource.ORE] if resources.has_key(
            Resource.ORE) else 0
        self.resourcesAvailable[Resource.SHEEP] = resources[Resource.SHEEP] if resources.has_key(
            Resource.SHEEP) else 0

        self.color = color

    def __init__(self):
        self.__init__(0, [], False, False, [], {}, PlayerColor.BLANK)


class PlayerColor(Enum):
    WHITE = 0
    RED = 1
    BLUE = 2
    ORANGE = 3
    BLANK = 4
