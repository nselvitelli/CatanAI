from Actions.Action import Action
from Node import NodePiece
from Resource import Resource


class BuildSettlement(Action):

    def __init__(self, nodeID) -> None:
        super().__init__()
        self.nodeID = nodeID

    def apply(self, state):
        newState = state.getCopy()

        newNode = newState.board.nodes[self.nodeID].getCopy()
        newNode.piece = (NodePiece.SETTLEMENT, newState.whoseTurn)
        newState.board.node[self.nodeID] = newNode

        playerData = newState.playerDataDict[newState.whoseTurn]
        playerData.resourcesAvailable[Resource.LOG] -= 1
        playerData.resourcesAvailable[Resource.BRICK] -= 1
        playerData.resourcesAvailable[Resource.SHEEP] -= 1
        playerData.resourcesAvailable[Resource.WHEAT] -= 1

        playerData.victoryPoints += 1

        return newState
