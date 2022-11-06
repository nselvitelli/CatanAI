from Actions.Action import Action


class Monopoly(Action):

    def __init__(self, resource) -> None:
        super().__init__()
        self.resource = resource

    def apply(self, state):
        newState = state.getCopy()

        stealCount = 0
        for playerColor in newState.playerDataDict:
            if playerColor != newState.whoseTurn:
                stealCount += newState.playerDataDict[playerColor].resourcesAvailable[self.resource]
                newState.playerDataDict[playerColor].resourcesAvailable[self.resource] = 0

        newState.playerDataDict[newState.whoseTurn].resourcesAvailable[self.resource] += stealCount
        return newState
