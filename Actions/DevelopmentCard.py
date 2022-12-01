from Actions.Action import Action
import random

from DevCard import DevCardName
from Resource import Resource


class DevelopmentCard(Action):

    def __init__(self, debug=False) -> None:
        super().__init__(debug)

    def apply(self, state):
        newState = state.getCopy()

        playerData = newState.playerDataList[newState.whoseTurn]

        stealNum = random.randint(0, len(newState.devCards) - 1)
        newDevCard = newState.devCards.pop(stealNum)

        if newDevCard in [DevCardName.CHAPEL, DevCardName.GREAT_HALL, DevCardName.LIBRARY, DevCardName.MARKET, DevCardName.UNIVERSITY]:
            playerData.victoryPoints += 1
        playerData.pendingDevCards.append(newDevCard)
        
        playerData.resourcesAvailable[Resource.WHEAT] -= 1
        playerData.resourcesAvailable[Resource.SHEEP] -= 1
        playerData.resourcesAvailable[Resource.ORE] -= 1

        return newState

    def getActionAsString(self):
            return "BuyDevCard"