from Actions.Action import Action, EAction


class EndTurn(Action):

    def __init__(self, debug=False) -> None:
        super().__init__(debug)

    def apply(self, state):
        nextState = state.getCopy()

        currentPlayer = nextState.playerDataList[nextState.whoseTurn]

        currentPlayer.devCards.extend(currentPlayer.pendingDevCards)
        currentPlayer.pendingDevCards.clear()

        nextState.whoseTurn = (nextState.whoseTurn + 1) % len(nextState.playerDataList)

        nextState.necessaryActions.append(EAction.ROLLDICE)

        return nextState

    def getActionAsString(self):
        return "_EndTurn_"