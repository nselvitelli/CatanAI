from Actions.Action import Action
from Resource import Resource


class BuildRoad(Action):

    def __init__(self, edgeID) -> None:
        super().__init__()
        self.edgeID = edgeID

    def apply(self, state):
        newState = state.getCopy()

        newEdge = newState.board.edges[self.edgeID].getCopy()

        playerData = newState.playerDataList[newState.whoseTurn]

        newEdge.playerColor = playerData.color
        newState.board.edges[self.edgeID] = newEdge

        playerData.resourcesAvailable[Resource.LOG] -= 1
        playerData.resourcesAvailable[Resource.BRICK] -= 1

        # here we should check if we have a new longest road, and if that road is longer than the current longest
        # probably should store longestroad as a tuple of (length, player)

        previousLargestArmyPlayer = newState.playerDataList[newState.largestArmy] if newState.largestArmy != -1 else None
        #Gonna need to be recursive, but track a global explored set
        #algorithm:
        #keep track of explored set of roads
        #maxLength = 0
        #rexplored = []
        #for each settlement in player.settlements
            #maxLength = max(maxLength, exploreNode(settlement, 0, explored))


        #exploreNode(nodeID, currentLength, explored):
            #IF NODE IS ENEMY PLAYER COLOR, RETURN currentLength
            #maxLength = currentLength
            #for each adjacent road of player color NOT in explored set
                #add road to explored set
                #maxLength = max(maxLength, exploreNode(otherNodeOnRoad, currentLength + 1, explored))
            #return maxLength


        return newState

    def getActionAsString(self):
        return "BuildRoad on " + str('%02d' % self.edgeID)
