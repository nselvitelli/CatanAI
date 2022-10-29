from Resource import Resource
from PlayerColor import PlayerColor


class PlayerData:

    def __init__(self, victoryPoints=0, devCards=[], settlements=[], resources={}, armySize=0, color=PlayerColor.BLANK) -> None:
        self.victoryPoints = victoryPoints

        # Note: NOT a deep copy (don't think it needs to be, never edit devcards)
        self.devCards = []
        for devCard in devCards:
            self.devCards.append(devCard)

        self.settlements = []
        for settlement in settlements:
            self.settlements.append(settlement)

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

        self.armySize = armySize
        self.color = color

    def getTotalResources(self):
        count = 0
        for key in self.resourcesAvailable:
            count += self.resourcesAvailable[key]
        return count
