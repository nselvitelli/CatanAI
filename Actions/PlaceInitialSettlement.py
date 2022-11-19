from Actions.Action import Action
from Node import NodePiece, Port
from Resource import Resource


class PlaceInitialSettlement(Action):

    def __init__(self, nodeID, isLastPlacedSettlement) -> None:
        super().__init__()
        self.nodeID = nodeID
        self.isLastPlacedSettlement = isLastPlacedSettlement


    def apply(self, state):
        newState = state.getCopy()

        playerData = newState.playerDataList[newState.whoseTurn]

        newNode = newState.board.nodes[self.nodeID].getCopy()
        newNode.piece = (NodePiece.SETTLEMENT, playerData.color)
        newState.board.node[self.nodeID] = newNode
        
        if self.isLastPlacedSettlement:
            for tileID, tile in state.board.tiles.items():
                if self.nodeID in tile.nodes:
                    playerData.resourcesAvailable[tile.resource] += 1

        if newNode.port != Port.EMPTY:
            playerData.portsAvailable.add(newNode.port)

        playerData.settlements.append(self.nodeID)

        playerData.victoryPoints += 1

        return newState

    def getActionAsString(self):
        return "BuildSettlement on " + str(self.nodeID) 