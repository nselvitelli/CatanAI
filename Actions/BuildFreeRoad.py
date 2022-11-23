from Actions.Action import Action
from Resource import Resource


class BuildFreeRoad(Action):

    def __init__(self, edgeID, necessaryActions) -> None:
        super().__init__()
        self.edgeID = edgeID
        self.necessaryActions = necessaryActions

    def apply(self, state):
        newState = state.getCopy()

        newState.necessaryActions.clear()

        newEdge = newState.board.edges[self.edgeID].getCopy()

        playerData = newState.playerDataList[newState.whoseTurn]

        newEdge.playerColor = playerData.color
        newState.board.edges[self.edgeID] = newEdge

        newState.necessaryActions = self.necessaryActions

        return newState
    
    def getActionAsString(self):
        return "BuildFreeRoad on " + str('%02d' % self.edgeID)
