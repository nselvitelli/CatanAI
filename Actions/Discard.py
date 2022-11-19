from Actions.Action import Action


class Discard(Action):

    def __init__(self, resource, necessaryActions) -> None:
        super().__init__()
        self.resource = resource
        self.necessaryActions = necessaryActions

    def apply(self, state):
        nextState = state.getCopy()

        nextState.playerData[nextState.whoseTurn].resourcesAvailable.remove(self.resource)
        
        nextState.necessaryActions = self.necessaryActions


        return nextState

    def getActionAsString(self):
        return "Discard " + str(self.resource.name)