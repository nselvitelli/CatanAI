from Actions.Action import Action
from Resource import Resource


class BuildRoad(Action):

    def __init__(self, edgeID) -> None:
        super().__init__()
        self.edgeID = edgeID

    def apply(self, state):
        newState = state.getCopy()

        newEdge = newState.board.edges[self.edgeID].getCopy()
        newEdge.playerIndex = newState.whoseTurn
        newState.board.edges[self.edgeID] = newEdge

        playerData = newState.playerDataList[newState.whoseTurn]
        playerData.resourcesAvailable[Resource.LOG] -= 1
        playerData.resourcesAvailable[Resource.BRICK] -= 1

        return newState
