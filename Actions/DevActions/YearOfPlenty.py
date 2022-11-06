from Actions.Action import Action


class YearOfPlenty(Action):

    def __init__(self, resource1, resource2) -> None:
        super().__init__()
        self.resource1 = resource1
        self.resource2 = resource2

    def apply(self, state):
        newState = state.getCopy()
        playerData = newState.playerDataDict[newState.whoseTurn]
        playerData.resourcesAvailable[self.resource1] += 1
        playerData.resourcesAvailable[self.resource2] += 1
        return newState
