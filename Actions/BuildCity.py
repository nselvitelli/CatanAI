from Actions.Action import Action
from Node import NodePiece
from Resource import Resource


class BuildCity(Action):

    def __init__(self, nodeID) -> None:
        super().__init__()
        self.nodeID = nodeID

    def apply(self, state):
        newState = state.getCopy()

        playerData = newState.playerDataList[newState.whoseTurn]

        newNode = newState.board.nodes[self.nodeID].getCopy()
        newNode.piece = (NodePiece.CITY, playerData.color)
        newState.board.nodes[self.nodeID] = newNode

        
        playerData.resourcesAvailable[Resource.WHEAT] -= 2
        playerData.resourcesAvailable[Resource.ORE] -= 3

        playerData.victoryPoints += 1

        return newState

    def getActionAsString(self):
        return "BuildCity on " + str(self.nodeID)