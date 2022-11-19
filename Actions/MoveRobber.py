from Actions.Action import Action
import random


class MoveRobber(Action):

    def __init__(self, tileID, stealPlayer, necessaryActions) -> None:
        super().__init__()
        self.tileID = tileID
        self.stealPlayer = stealPlayer
        self.necessaryActions = necessaryActions

    def apply(self, state):
        newState = state.getCopy()
        # moves robber to new tile
        newState.board.robber_tile = self.tileID

        # performs steal
        stealData = newState.playerDataDict[self.stealPlayer]

        totalResourceCount = stealData.getTotalResources()

        stealNum = random.randint(1, totalResourceCount)

        count = 0
        for key in stealData.resourcesAvailable:
            if count + stealData.resourcesAvailable[key] >= stealNum:
                stealData.resourcesAvailable[key] -= 1
                newState.playerDataDict[newState.whoseTurn].resourcesAvailable[key] += 1
                break
            count += stealData.resourcesAvailable[key]

        newState.necessaryActions.extend(self.necessaryActions)

        return newState
