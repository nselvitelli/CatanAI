from Actions.Action import Action


class NextPlayer(Action):

    # TODO: we need to come up with some way of tracking turn order...
    def __init__(self, necessaryActions) -> None:
        super().__init__()
        self.necessaryActions = necessaryActions

    def apply(self, state):
        nextState = state.getCopy()

        nextState.whoseTurn = (nextState.whoseTurn + 1) % len(nextState.playerDataList)

        nextState.necessaryActions.extend(self.necessaryActions)

        return nextState


    def getActionAsString(self):
        return "NextPlayer"