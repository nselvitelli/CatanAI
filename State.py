from mimetypes import init
from Actions.BuildRoad import BuildRoad

from Resource import Resource

class State:

    def __init__(self, board, playerDataDict, devCards, whoseTurn) -> None:
        self.board = board
        self.playerDataDict = playerDataDict
        self.devCards = devCards
        self.whoseTurn = whoseTurn # this is a color

    def getValidActions(self):
        currentPlayer = self.playerDataDict[self.whoseTurn]
        resourcesAvailable = currentPlayer.resourcesAvailable

        validActions = []

        if resourcesAvailable[Resource.BRICK] >= 1 and resourcesAvailable[Resource.LOG] >= 1:
            validRoadLocations = set()
            for settlementNodeID in currentPlayer.firstSettlements:
                validRoadLocations.union(set(self.board.bfsEndpoint(settlementNodeID, self.whoseTurn)))
            for roadLocation in validRoadLocations:
                validActions.append(BuildRoad(roadLocation))

        if resourcesAvailable[Resource.BRICK] >= 1 and resourcesAvailable[Resource.LOG] >= 1 and resourcesAvailable[Resource.SHEEP] >= 1 and resourcesAvailable[Resource.WHEAT] >= 1:
            


#end State