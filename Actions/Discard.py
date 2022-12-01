from Actions.Action import Action


class Discard(Action):

    def __init__(self, resource, necessaryActions, debug=False) -> None:
        super().__init__(debug)
        self.resource = resource
        self.necessaryActions = necessaryActions

    def apply(self, state):
        nextState = state.getCopy()

        nextState.playerDataList[nextState.whoseTurn].resourcesAvailable[self.resource] -= 1
        
        nextState.necessaryActions = self.necessaryActions

        return nextState

    def getActionAsString(self):
        return "Discard " + str(self.resource.name)