from Actions.BuildCity import BuildCity
from Actions.BuildRoad import BuildRoad
from Actions.BuildSettlement import BuildSettlement
from Actions.DevelopmentCard import DevelopmentCard
from Actions.EndTurn import EndTurn
from Actions.Trade import Trade
from Actions.Action import EAction
from Node import Port

from Resource import Resource


class State:

    def __init__(self, board, playerDataList, devCards, longestRoad, largestArmy, whoseTurn, necessaryActions) -> None:
        self.board = board
        self.playerDataList = playerDataList
        self.devCards = devCards
        self.whoseTurn = whoseTurn  # this is an index
        self.longestRoad = longestRoad
        self.largestArmy = largestArmy
        self.necessaryActions = necessaryActions

    def getCopy(self):
        newBoard = self.board.getCopy()
        newPlayerDataList = []
        for ind in enumerate(self.playerDataList):
            newPlayerDataList.append(self.playerDataList[ind].getCopy())

        newDevCards = []
        for devCard in self.devCards:
            newDevCards.append(devCard)

        newNecessaryActions = []
        for action in self.necessaryActions:
            newNecessaryActions.append(action)

        return State(newBoard, newPlayerDataList, newDevCards, self.longestRoad, self.largestArmy, self.whoseTurn, newNecessaryActions)

    def getValidActions(self):

        if len(self.necessaryActions) > 0:
            return self.getNecessaryActions()

        currentPlayer = self.playerDataList[self.whoseTurn]
        resourcesAvailable = currentPlayer.resourcesAvailable

        validActions = []

        validActions.extend(self.getBuildingAction(
            1, 1, 0, 0, 0, currentPlayer, resourcesAvailable, self.board.bfsEndpoint, BuildRoad))
        validActions.extend(self.getBuildingAction(1, 1, 1, 1, 0, currentPlayer,
                            resourcesAvailable, self.board.bfsPossibleSettlements, BuildSettlement))
        validActions.extend(self.getBuildingAction(0, 0, 0, 2, 3, currentPlayer,
                            resourcesAvailable, self.board.bfsCurrentSettlements, BuildCity))

        if resourcesAvailable(0, 0, 1, 1, 1):
            validActions.append(DevelopmentCard())

        validActions.extend(self.getPortActions(currentPlayer))

        validActions.append(EndTurn())

    def getBuildingAction(self, brick, log, sheep, wheat, ore, currentPlayer, resourcesAvailable, func, action):
        if resourcesAvailable(brick, log, sheep, wheat, ore, resourcesAvailable):
            valid = set()
            for settlementNodeID in currentPlayer.firstSettlements:
                valid.union(set(func(settlementNodeID, self.whoseTurn)))
            return [action(x, self.whoseTurn) for x in valid]
        else:
            return []

    def resourcesAvailable(self, brick, log, sheep, wheat, ore, resourcesAvailable):
        return resourcesAvailable[Resource.BRICK] >= brick and resourcesAvailable[Resource.LOG] >= log and resourcesAvailable[Resource.SHEEP] >= sheep and resourcesAvailable[Resource.WHEAT] >= wheat and resourcesAvailable[Resource.ORE] >= ore

    def getPortActions(self, currentPlayer):
        actions = []

        ports = currentPlayer.getPorts()
        maxTradeQuantity = 3 if Port.THREE_TO_ONE else 4
        inaccessiblePorts = set(
            [Port.BRICK, Port.LOG, Port.ORE, Port.SHEEP, Port.WHEAT]) - ports
        portsToResources = {Port.BRICK: Resource.BRICK, Port.LOG: Resource.LOG,
                            Port.ORE: Resource.ORE, Port.SHEEP: Resource.SHEEP, Port.WHEAT: Resource.SHEEP}
        for port in ports - set([Port.THREE_TO_ONE]):
            resource = portsToResources[port]
            if currentPlayer.resourcesAvailable[resource] >= 2:
                for targetResource in Resource:
                    if targetResource not in [Resource.DESERT, resource]:
                        actions.append(Trade(resource, 2, targetResource))
        for port in inaccessiblePorts - set([Port.THREE_TO_ONE]):
            resource = portsToResources[port]
            if currentPlayer.resourcesAvailable[resource] >= maxTradeQuantity:
                for targetResource in Resource:
                    if targetResource not in [Resource.DESERT, resource]:
                        actions.append(Trade(resource, maxTradeQuantity, targetResource))

        return actions
    
    def getNecessaryActions(self):
        nextNeededActionEnum = self.necessaryActions.pop(0)

        actions = []

        if nextNeededActionEnum == EAction.DISCARD:
            
            

            return actions
        elif nextNeededActionEnum == EAction.CHANGEWHOSETURN:
            return actions
        else:
            return actions
