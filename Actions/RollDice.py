from Actions.Action import Action
from Node import NodePiece
from MoveRobber import MoveRobber
import random


class RollDice(Action):

    def __init__(self, discardCards, robberTileID, robberStealPlayer) -> None:
        super().__init__()
        self.discardCards = discardCards
        self.robberTileID = robberTileID
        self.robberStealPlayer = robberStealPlayer

    def apply(self, state):
        newState = state.getCopy()

        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        rollVal = d1 + d2

        if rollVal == 7:
            if (self.robberTileID == None):
                l = 0
                # need to take in user data here!
                # discardcards should be a dict of each player??????
                # each player needs to choose in order which cards they discard i think...
            # for each player check if they have 8 cards
            # TODO: we need to take in information for discarding / movingrobber
            moveRobber = MoveRobber(self.robberTileID, self.robberStealPlayer)

        else:
            for tileNum in newState.board.tiles:
                tile = newState.board.tiles[tileNum]
                if tile.number == rollVal and tileNum != newState.board.robber_tile:
                    for nodeNum in tile.nodes:
                        node = newState.board.nodes[nodeNum]
                        if node.piece[0] == NodePiece.SETTLEMENT:
                            playerData = newState.playerDataDict[node.piece[1]]
                            playerData.resourcesAvailable[tile.resource] += 1
                        elif node.piece[0] == NodePiece.CITY:
                            playerData = newState.playerDataDict[node.piece[1]]
                            playerData.resourcesAvailable[tile.resource] += 2

        return newState
