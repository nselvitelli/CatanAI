from Actions.Action import Action, EAction
from Actions.MoveRobber import MoveRobber
from PlayerColor import PlayerColor
from DevCard import DevCardName

# Action class for playing a knight


class Knight(Action):

    def __init__(self) -> None:
        super().__init__()

    def apply(self, state):
        newState = state.getCopy()
        newState.necessaryActions.insert(0, EAction.MOVEROBBER)

        # corrects largest army if necessary
        maxKnights = 0
        for key in newState.playerDataDict:
            maxKnights = max(maxKnights, newState.playerDataDict[key].armySize)

        playerTurnData = newState.playerDataDict[state.whoseTurn]
        if maxKnights == playerTurnData.armySize and maxKnights >= 2:
            if state.largestArmy != PlayerColor.BLANK:
                newState.playerDataDict[state.largestArmy].victoryPoints -= 2
            state.largestArmy = state.whoseTurn
            playerTurnData.victoryPoints += 2
        playerTurnData.armySize += 1

        # removes used card from player's hand
        for index, devCard in enumerate(playerTurnData.devCards):
            if devCard.name == DevCardName.KNIGHT:
                playerTurnData.devCards.pop(index)
                break
        return newState

    # remove card from player hand

    def getActionAsString(self):
            return "Play Knight DevCard"