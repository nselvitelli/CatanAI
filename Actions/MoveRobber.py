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
        if self.stealPlayer != None:
            stealData = newState.getPlayerWithColor(self.stealPlayer.color)

            totalResourceCount = stealData.getTotalResources()
            if totalResourceCount > 0 :
                stealNum = random.randint(1, totalResourceCount)

                count = 0
                for key in stealData.resourcesAvailable:
                    if count + stealData.resourcesAvailable[key] >= stealNum:
                        stealData.resourcesAvailable[key] -= 1
                        newState.playerDataList[newState.whoseTurn].resourcesAvailable[key] += 1
                        break
                    count += stealData.resourcesAvailable[key]

        newState.necessaryActions = self.necessaryActions

        return newState

    def getActionAsString(self):
        player = str(None) if self.stealPlayer == None else str(self.stealPlayer.color)
        return "MoveRobber to " + str(self.tileID) + ", steal from Player " + player