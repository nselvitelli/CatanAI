from Actions.Action import Action
from Node import NodePiece
from Resource import Resource


class BuildCity(Action):

    def __init__(self, nodeID) -> None:
        super().__init__()
        self.nodeID = nodeID

    def apply(self, state):
        newState = state.getCopy()

        newNode = newState.board.nodes[self.nodeID].getCopy()
        newNode.piece = (NodePiece.CITY, newState.whoseTurn)
        newState.board.node[self.nodeID] = newNode

        playerData = newState.playerDataDict[newState.whoseTurn]
        playerData.resourcesAvailable[Resource.WHEAT] -= 2
        playerData.resourcesAvailable[Resource.ORE] -= 3

        playerData.victoryPoints += 1

        return newState
