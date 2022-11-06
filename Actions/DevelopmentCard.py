from Actions.Action import Action
import random


class DevelopmentCard(Action):

    def __init__(self) -> None:
        super().__init__()

    def apply(self, state):
        newState = state.getCopy()

        stealNum = random.randint(0, len(newState.devCards) - 1)
        newDevCard = newState.devCards.pop(stealNum)
        newState.playerDataDict[newState.whoseTurn].devCards.append(newDevCard)

        return newState
