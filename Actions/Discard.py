from Actions.Action import Action


class Discard(Action):

    def __init__(self, resource) -> None:
        super().__init__()
        self.resource = resource

    def apply(self, state):
        nextState = state.getCopy()

        nextState.playerData[nextState.whoseTurn].resourcesAvailable.remove(self.resource)

        return nextState