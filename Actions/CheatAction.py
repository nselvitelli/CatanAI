from Actions.Action import Action, EAction
import State
from Resource import Resource


class CheatAction(Action):

    def __init__(self) -> None:
        super().__init__()

    def apply(self, state):
        nextState = state.getCopy()

        currentPlayer = nextState.playerDataList[nextState.whoseTurn]

        currentPlayer.devCards.extend(State.getDevCardPool()) # get all dev cards

        currentPlayer.resourcesAvailable[Resource.WHEAT] = 100
        currentPlayer.resourcesAvailable[Resource.BRICK] = 100
        currentPlayer.resourcesAvailable[Resource.LOG] = 100
        currentPlayer.resourcesAvailable[Resource.ORE] = 100
        currentPlayer.resourcesAvailable[Resource.SHEEP] = 100

        return nextState

    def getActionAsString(self):
        return "CHEATING (all dev cards + all resources)"