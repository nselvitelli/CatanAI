from Actions.Action import Action
import random

from DevCard import DevCardName
from Resource import Resource


class DevelopmentCard(Action):

    def __init__(self, debug=False) -> None:
        super().__init__(debug)
        self.devCardNumber = -1

    def getAllOutcomes(self, state):
        totalDevCards = len(state.devCards)
        outcomes = []
        i = 0
        while i < totalDevCards:
            outcomes.append((1/totalDevCards, i))
            i += 1
        return outcomes

    def applyExact(self, state, value):
        self.devCardNumber = value
        return self.apply(state)

    def apply(self, state):
        newState = state.getCopy()

        playerData = newState.playerDataList[newState.whoseTurn]

        devNum = self.devCardNumber
        if devNum == -1:
            devNum = random.randint(0, len(newState.devCards) - 1)
        newDevCard = newState.devCards.pop(devNum)

        if newDevCard in [DevCardName.CHAPEL, DevCardName.GREAT_HALL, DevCardName.LIBRARY, DevCardName.MARKET, DevCardName.UNIVERSITY]:
            playerData.victoryPoints += 1
        playerData.pendingDevCards.append(newDevCard)

        playerData.resourcesAvailable[Resource.WHEAT] -= 1
        playerData.resourcesAvailable[Resource.SHEEP] -= 1
        playerData.resourcesAvailable[Resource.ORE] -= 1

        self.devCardNumber = -1
        return newState

    def getActionAsString(self):
        return "BuyDevCard"
