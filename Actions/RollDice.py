from Actions.Action import Action, EAction
from Node import NodePiece
import random


class RollDice(Action):

    def __init__(self, necessaryActions) -> None:
        super().__init__()
        self.necessaryActions = necessaryActions

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

        newState.necessaryActions.extend(self.necessaryActions)

        return newState

    def getActionAsString(self):
        return "RollDice"