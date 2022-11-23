from Actions.Action import Action
from DevCard import DevCardName


class Monopoly(Action):

    def __init__(self, resource) -> None:
        super().__init__()
        self.resource = resource

    def apply(self, state):
        newState = state.getCopy()

        currentPlayer = newState.playerDataList[newState.whoseTurn]

        stealCount = 0
        for idx,player in enumerate(set(newState.playerDataList) - set([currentPlayer])):
            if idx != newState.whoseTurn:
                stealCount += player.resourcesAvailable[self.resource]
                print(currentPlayer.color.name, "stole", str(stealCount), self.resource.name, "from", player.color.name)
                player.resourcesAvailable[self.resource] = 0

        currentPlayer.resourcesAvailable[self.resource] += stealCount
        currentPlayer.devCards.remove(DevCardName.MONOPOLY)

        return newState

    def getActionAsString(self):
        return "Play Monopoly DevCard to get " + str(self.resource.name) + " from all players"