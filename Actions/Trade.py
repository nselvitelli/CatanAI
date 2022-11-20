from Actions.Action import Action
from Node import Port


class Trade(Action):

    def __init__(self, resource, quantity, targetResource) -> None:
        super().__init__()
        self.resource = resource
        self.quantity = quantity
        self.targetResource = targetResource


    def apply(self, state):
        newState = state.getCopy()

        playerData = newState.playerDataList[newState.whoseTurn]
        playerData.resourcesAvailable[self.resource] -= self.quantity
        playerData.resourcesAvailable[self.targetResource] += 1

        return newState

    def getActionAsString(self):
        return "Trade " + str(self.quantity) + " " + str(self.resource.name) + " for 1 " + str(self.targetResource.name)