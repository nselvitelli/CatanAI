from mimetypes import init
from Actions.BuildCity import BuildCity
from Actions.BuildRoad import BuildRoad
from Actions.BuildSettlement import BuildSettlement
from Actions.DevelopmentCard import DevelopmentCard

from Resource import Resource


class State:

    def __init__(self, board, playerDataDict, devCards, longestRoad, largestArmy, whoseTurn) -> None:
        self.board = board
        self.playerDataDict = playerDataDict
        self.devCards = devCards
        self.whoseTurn = whoseTurn  # this is a color
        self.longestRoad = longestRoad
        self.largestArmy = largestArmy

    def getValidActions(self):
        currentPlayer = self.playerDataDict[self.whoseTurn]
        resourcesAvailable = currentPlayer.resourcesAvailable

        validActions = []

        validActions.extend(self.getBuildingAction(1,1,0,0,0,currentPlayer,resourcesAvailable,self.board.bfsEndpoint,BuildRoad))
        validActions.extend(self.getBuildingAction(1,1,1,1,0,currentPlayer,resourcesAvailable,self.board.bfsPossibleSettlements,BuildSettlement))
        validActions.extend(self.getBuildingAction(0,0,0,2,3,currentPlayer,resourcesAvailable,self.board.bfsCurrentSettlements,BuildCity))

        if resourcesAvailable(0,0,1,1,1):
            validActions.append(DevelopmentCard(currentPlayer))

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


# end State
