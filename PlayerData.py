from Resource import Resource
from PlayerColor import PlayerColor


class PlayerData:

    def __init__(self, agent, victoryPoints=0, devCards=[], settlements=[], resources={}, armySize=0, color=PlayerColor.BLANK, pendingDevCards = []) -> None:
        self.agent = agent
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

        newPendingDevCards = []
        for card in self.pendingDevCards:
            newPendingDevCards.append(card)

        return PlayerData(self.agent, self.victoryPoints, newDevCards, newSettlements, newResources, self.armySize, self.color, newPendingDevCards)

    def getPorts(self):
        return self.portsAvailable
    
    def getPlayerDifferences(self, prevPlayer, board):
        message = "Player " + self.color.name + ":\n"

        if self.victoryPoints != prevPlayer.victoryPoints:
            message += "\tVP: " + str(prevPlayer.victoryPoints) + " -> " + str(self.victoryPoints)+ "\n"
        else:
            message += "\tVP: " + str(self.victoryPoints) + "\n"
        
        if len(self.devCards) < len(prevPlayer.devCards):
            trackerCards = self.devCards.copy()
            usedCards = []
            for i in prevPlayer.devCards:
                if i not in trackerCards:
                    usedCards.append(i.name)
                else:
                    trackerCards.remove(i)
            message += "\tUsed DevCards: " + str(usedCards) + "\n"
        
        if len(self.devCards) > 0:
            message += "\tDevCards Available: " + str(list(map(lambda a: a.name, self.devCards))) + "\n"

        if len(self.pendingDevCards) > 0:
            message += "\tDevCards Pending: " + str(list(map(lambda a: a.name, self.pendingDevCards))) + "\n"

        settlementLocTypeTupleList = list(map(lambda a: (a, board.nodes[a].piece[0].name), self.settlements))

        message += "\tCurrent Settlements: " + str(settlementLocTypeTupleList) + "\n"

        if self.resourcesAvailable != prevPlayer.resourcesAvailable:
            message += "\tResources:\n"
            for key, value in self.resourcesAvailable.items():
                prevAmt = prevPlayer.resourcesAvailable[key]
                message += "\t - " + key.name + ": " + str(value)
                if value > prevAmt:
                    message += " (+" + str(value - prevAmt) + ")\n"
                elif value < prevAmt:
                    message += " (" + str(value - prevAmt) + ")\n"
                else:
                    message += "\n"
        
        if self.armySize > 0:
            message += "\tArmySize: " + (str(self.armySize) if self.armySize == prevPlayer.armySize else (str(prevPlayer.armySize) + " -> " + str(self.armySize))) + "\n"
        
        if len(self.portsAvailable) > 0:
            message += "\tPorts owned: " + str(list(map(lambda a: a.name, self.portsAvailable)))

        return message
