from Actions.Action import Action, EAction
from Actions.BuildRoad import BuildRoad
from DevCard import DevCardName
from Resource import Resource


class RoadBuilding(Action):

    def __init__(self) -> None:
        super().__init__()

    def apply(self, state):
        newState = state.getCopy()
        newState.necessaryActions.clear()
        newState.necessaryActions.append(EAction.BUILDFREEROAD)
        newState.necessaryActions.append(EAction.BUILDFREEROAD)
        newState.necessaryActions.extend(state.necessaryActions)

        newState.playerDataList[newState.whoseTurn].devCards.remove(DevCardName.ROAD_BUILDING)

        return newState

    def getActionAsString(self):
        return "Play RoadBuilding DevCard"