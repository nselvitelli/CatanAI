from Actions.Action import Action
from DevCard import DevCardName


class Monopoly(Action):

    def __init__(self, resource) -> None:
        super().__init__()
        self.resource = resource

    def apply(self, state):
        newState = state.getCopy()

        stealCount = 0
        for idx,player in enumerate(newState.playerDataList):
            if idx != newState.whoseTurn:
                stealCount += newState.getPlayerWithColor(player).resourcesAvailable[self.resource]
                newState.playerDataList[player].resourcesAvailable[self.resource] = 0

        newState[newState.whoseTurn].resourcesAvailable[self.resource] += stealCount

        newState.playerDataList[newState.whoseTurn].devCards.remove(DevCardName.MONOPOLY)

        return newState

    def getActionAsString(self):
        return "Play Monopoly DevCard to get " + str(self.resource) + " from all players"