from Actions.Action import Action, EAction
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
            for player in state.playerDataList:
                newState.necessaryActions.append(EAction.NEXTPLAYER)
                for i in range(max(0, len(player.resourcesAvailable.items()) - 7)):
                    newState.necessaryActions.append(EAction.DISCARD)
            newState.necessaryAction.append(EAction.MOVEROBBER)

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
