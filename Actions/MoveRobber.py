from Actions.Action import Action
import random


class MoveRobber(Action):

    def __init__(self, tileID, stealPlayer, necessaryActions, debug=False) -> None:
        super().__init__(debug)
        self.tileID = tileID
        self.stealPlayer = stealPlayer
        self.necessaryActions = necessaryActions
        self.stealValue = 0

    def getAllOutcomes(self, state) :
        if self.stealPlayer == None :
            return [(1, 0)]
        totalResources = state.getPlayerWithColor(self.stealPlayer.color).getTotalResources()
        if totalResources == 0 :
            return [(1, 0)]
        outcomes = []
        i = 1
        while i <= totalResources :
            outcomes.append((1 / totalResources, i))
            i += 1
        return outcomes

    def applyExact(self, state, value) :
        self.stealValue = value
        return self.apply(state)

    def apply(self, state):
        newState = state.getCopy()
        # moves robber to new tile
        newState.board.robber_tile = self.tileID

        # performs steal
        if self.stealPlayer != None:
            stealData = newState.getPlayerWithColor(self.stealPlayer.color)

            totalResourceCount = stealData.getTotalResources()
            if totalResourceCount > 0 :
                stealNum = self.stealValue
                if stealNum == 0 :
                    stealNum = random.randint(1, totalResourceCount)

                count = 0
                for key in stealData.resourcesAvailable:
                    if count + stealData.resourcesAvailable[key] >= stealNum:
                        stealData.resourcesAvailable[key] -= 1
                        newState.playerDataList[newState.whoseTurn].resourcesAvailable[key] += 1
                        break
                    count += stealData.resourcesAvailable[key]

        newState.necessaryActions = self.necessaryActions
        self.stealValue = 0
        return newState

    def getActionAsString(self):
        player = str(None) if self.stealPlayer == None else str(self.stealPlayer.color.name)
        return "MoveRobber to " + str(self.tileID) + ", steal from Player " + player