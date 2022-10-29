from mimetypes import init
from Actions.BuildCity import BuildCity
from Actions.BuildRoad import BuildRoad
from Actions.BuildSettlement import BuildSettlement

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

        if resourcesAvailable[Resource.BRICK] >= 1 and resourcesAvailable[Resource.LOG] >= 1:
            validRoadLocations = set()
            for settlementNodeID in currentPlayer.firstSettlements:
                validRoadLocations.union(
                    set(self.board.bfsEndpoint(settlementNodeID, self.whoseTurn)))
            for roadLocation in validRoadLocations:
                validActions.append(BuildRoad(roadLocation, self.whoseTurn))

        if resourcesAvailable[Resource.BRICK] >= 1 and resourcesAvailable[Resource.LOG] >= 1 and resourcesAvailable[Resource.SHEEP] >= 1 and resourcesAvailable[Resource.WHEAT] >= 1:
            validSettlementLocations = set()
            for settlementNodeID in currentPlayer.firstSettlements:
                validSettlementLocations.union(
                    set(self.board.bfsPossibleSettlements(settlementNodeID, self.whoseTurn)))
            for settlementLocation in validSettlementLocations:
                validActions.append(BuildSettlement(
                    settlementLocation, self.whoseTurn))

        if resourcesAvailable[Resource.WHEAT] >= 2 and resourcesAvailable[Resource.ORE] >= 3:
            validUpgradeableSettlements = set()
            for settlementNodeID in currentPlayer.firstSettlements:
                validUpgradeableSettlements.union(
                    set(self.board.bfsCurrentSettlements(settlementNodeID, self.whoseTurn)))
            for upgradeableSettlement in validUpgradeableSettlements:
                validActions.append(
                    BuildCity(upgradeableSettlement, self.whoseTurn))


# end State
