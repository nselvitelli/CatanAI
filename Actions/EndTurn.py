from Actions.Action import Action, EAction


class EndTurn(Action):

    def __init__(self) -> None:
        super().__init__()

    def apply(self, state):
        nextState = state.getCopy()

        currentPlayer = nextState.playerDataList[nextState.whoseTurn]

        currentPlayer.devCards.extend(currentPlayer.pendingDevCards)
        currentPlayer.pendingDevCards.clear()

        nextState.necessaryActions.append(EAction.NEXTPLAYER)
        nextState.necessaryActions.append(EAction.ROLLDICE)

        return nextState

    def getActionAsString(self):
        return "EndTurn"