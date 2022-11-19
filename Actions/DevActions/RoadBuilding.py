from Actions.Action import Action
from Actions.BuildRoad import BuildRoad
from Resource import Resource


class RoadBuilding(Action):

    def __init__(self, edgeID1, edgeID2) -> None:
        super().__init__()
        self.edgeID1 = edgeID1
        self.edgeID2 = edgeID2

    def apply(self, state):
        buildRoad1 = BuildRoad(self.edgeID1)
        buildRoad2 = BuildRoad(self.edgeID2)
        intermediateState = buildRoad1.apply(state)
        newState = buildRoad2.apply(intermediateState)

        playerData = newState.playerDataDict[newState.whoseTurn]
        playerData.resourcesAvailable[Resource.LOG] += 2
        playerData.resourcesAvailable[Resource.BRICK] += 2

        return newState

    def getActionAsString(self):
        return "Play RoadBuilding DevCard to build roads at " + str(self.edgeID1) + " and " + str(self.edgeID2)