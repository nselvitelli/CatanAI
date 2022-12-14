from Actions.Action import Action
from Node import NodePiece, Port
from Actions.Action import EAction
from Resource import Resource


class PlaceInitialSettlement(Action):

    def __init__(self, nodeID, isLastPlacedSettlement, necessaryActions, debug=False) -> None:
        super().__init__(debug)
        self.nodeID = nodeID
        self.isLastPlacedSettlement = isLastPlacedSettlement
        self.necessaryActions = necessaryActions


    def apply(self, state):
        newState = state.getCopy()

        newState.necessaryActions.clear()

        playerData = newState.playerDataList[newState.whoseTurn]

        newNode = newState.board.nodes[self.nodeID].getCopy()
        newNode.piece = (NodePiece.SETTLEMENT, playerData.color)
        newState.board.nodes[self.nodeID] = newNode
        


        if self.isLastPlacedSettlement:
            for tileID, tile in state.board.tiles.items():
                if self.nodeID in tile.nodes and tile.resource != Resource.DESERT:
                    playerData.resourcesAvailable[tile.resource] += 1
                    if self.debug:
                        print("\tadding resource:", tile.resource.name)

        if newNode.port != Port.EMPTY:
            playerData.portsAvailable.add(newNode.port)

        playerData.settlements.append(self.nodeID)

        playerData.victoryPoints += 1

        newState.necessaryActions.insert(0, EAction.BUILDFREEROAD)

        newState.necessaryActions.extend(self.necessaryActions)

        return newState

    def getActionAsString(self):
        return "BuildInitialSettlement on " + str('%02d' % self.nodeID) 