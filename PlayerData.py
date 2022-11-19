from Resource import Resource
from PlayerColor import PlayerColor


class PlayerData:

    def __init__(self, victoryPoints=0, devCards=[], settlements=[], resources={}, armySize=0, color=PlayerColor.BLANK, pendingDevCards = []) -> None:
        self.victoryPoints = victoryPoints
        self.devCards = devCards
        self.settlements = settlements
        self.pendingDevCards = pendingDevCards

        self.resourcesAvailable = {}
        self.resourcesAvailable[Resource.WHEAT] = resources[Resource.WHEAT] if Resource.WHEAT in resources else 0
        self.resourcesAvailable[Resource.BRICK] = resources[Resource.BRICK] if Resource.BRICK in resources else 0
        self.resourcesAvailable[Resource.LOG] = resources[Resource.LOG] if Resource.LOG in resources else 0
        self.resourcesAvailable[Resource.ORE] = resources[Resource.ORE] if Resource.ORE in resources else 0
        self.resourcesAvailable[Resource.SHEEP] = resources[Resource.SHEEP] if Resource.SHEEP in resources else 0

        self.armySize = armySize
        self.color = color
        self.portsAvailable = set()

    def getTotalResources(self):
        count = 0
        for key in self.resourcesAvailable:
            count += self.resourcesAvailable[key]
        return count

    def getCopy(self):
        newDevCards = []
        for devCard in self.devCards:
            newDevCards.append(devCard)

        newPendingDevCards = []
        for pDC in self.pendingDevCards:
            newPendingDevCards.append(pDC)

        newSettlements = []
        for settlement in self.settlements:
            newSettlements.append(settlement)

        newResources = {}
        for key in self.resourcesAvailable:
            newResources[key] = self.resourcesAvailable[key]

        return PlayerData(self.victoryPoints, newDevCards, newSettlements, newResources, self.armySize, self.color)

    def getPorts(self):
        return self.portsAvailable
