from Actions.Action import Action
from Node import NodePiece, Port
from Resource import Resource


class BuildSettlement(Action):

    def __init__(self, nodeID) -> None:
        super().__init__()
        self.nodeID = nodeID

    def apply(self, state):
        newState = state.getCopy()

        playerData = newState.playerDataList[newState.whoseTurn]

        newNode = newState.board.nodes[self.nodeID].getCopy()
        newNode.piece = (NodePiece.SETTLEMENT, playerData.color)
        newState.board.nodes[self.nodeID] = newNode
        
        playerData.resourcesAvailable[Resource.LOG] -= 1
        playerData.resourcesAvailable[Resource.BRICK] -= 1
        playerData.resourcesAvailable[Resource.SHEEP] -= 1
        playerData.resourcesAvailable[Resource.WHEAT] -= 1

        if newNode.port != Port.EMPTY:
            playerData.portsAvailable.add(newNode.port)

        playerData.settlements.append(self.nodeID)

        playerData.victoryPoints += 1

        return newState

    def getActionAsString(self):
        return "BuildSettlement on " + str(self.nodeID) 