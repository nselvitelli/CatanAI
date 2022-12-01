from Actions.Action import Action, EAction
from Node import NodePiece
import random


class RollDice(Action):

    def __init__(self, necessaryActions, debug=False) -> None:
        super().__init__(debug)
        self.necessaryActions = necessaryActions

    def apply(self, state):
        newState = state.getCopy()

        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        rollVal = d1 + d2

        if self.debug:
            print("\n----")
            print("Player " + state.playerDataList[state.whoseTurn].color.name + " rolled a [" + str(rollVal) + "]")
            print("----")

        newState.necessaryActions.clear()

        if rollVal == 7:

            playerIdx = newState.whoseTurn
            count = 0
            playerAmt = len(newState.playerDataList)

            while count < playerAmt:
                player = newState.playerDataList[playerIdx]

                numPlayerCards = 0
                for x in player.resourcesAvailable.values():
                    numPlayerCards += x

                cardsToRemove = int(numPlayerCards / 2) if numPlayerCards > 7 else 0

                if self.debug:
                    print("Player", player.color, "has [", numPlayerCards, "] cards, removing", cardsToRemove)

                for i in range(cardsToRemove):
                    newState.necessaryActions.append(EAction.DISCARD)
                
                newState.necessaryActions.append(EAction.NEXTPLAYER)
                playerIdx = (playerIdx + 1) % playerAmt
                count += 1

            newState.necessaryActions.append(EAction.MOVEROBBER)

        else:
            for tileNum in newState.board.tiles:
                tile = newState.board.tiles[tileNum]
                if tile.number == rollVal and tileNum != newState.board.robber_tile:
                    for nodeNum in tile.nodes:
                        node = newState.board.nodes[nodeNum]
                        if node.piece[0] == NodePiece.SETTLEMENT:
                            playerData = newState.getPlayerWithColor(node.piece[1])
                            playerData.resourcesAvailable[tile.resource] += 1
                        elif node.piece[0] == NodePiece.CITY:
                            playerData = newState.getPlayerWithColor(node.piece[1])
                            playerData.resourcesAvailable[tile.resource] += 2

        newState.necessaryActions.extend(self.necessaryActions)

        return newState

    def getActionAsString(self):
        return "RollDice"