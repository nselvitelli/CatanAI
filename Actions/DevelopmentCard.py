from Actions.Action import Action
import random

from DevCard import DevCardName


class DevelopmentCard(Action):

    def __init__(self) -> None:
        super().__init__()

    def apply(self, state):
        newState = state.getCopy()

        stealNum = random.randint(0, len(newState.devCards) - 1)
        newDevCard = newState.devCards.pop(stealNum)
        if newDevCard in [DevCardName.CHAPEL, DevCardName.GREAT_HALL, DevCardName.LIBRARY, DevCardName.MARKET, DevCardName.UNIVERSITY]:
            newState.playerDataDict[newState.whoseTurn].victoryPoints += 1
        else:
            newState.playerDataDict[newState.whoseTurn].pendingDevCards.append(newDevCard)

        return newState
