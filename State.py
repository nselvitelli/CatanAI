from mimetypes import init

from Resource import Resource

class State:

    def __init__(self, board, playerDataDict, devCards, whoseTurn) -> None:
        self.board = board
        self.playerDataDict = playerDataDict
        self.devCards = devCards
        self.whoseTurn = whoseTurn

    def getValidActions(self):
        currentPlayer = self.playerDataDict[self.whoseTurn]
        resourcesAvailable = currentPlayer.resourcesAvailable

        validActions = []

        if resourcesAvailable[Resource.BRICK] >= 1 and resourcesAvailable[Resource.LOG] >= 1:
            pass


#end State