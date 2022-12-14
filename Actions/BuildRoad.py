from Actions.Action import Action
from Resource import Resource


class BuildRoad(Action):

    def __init__(self, edgeID, debug=False) -> None:
        super().__init__(debug)
        self.edgeID = edgeID

    def apply(self, state):
        newState = state.getCopy()

        newEdge = newState.board.edges[self.edgeID].getCopy()

        playerData = newState.playerDataList[newState.whoseTurn]

        newEdge.playerColor = playerData.color
        newState.board.edges[self.edgeID] = newEdge

        playerData.resourcesAvailable[Resource.LOG] -= 1
        playerData.resourcesAvailable[Resource.BRICK] -= 1

        #LONGEST ROAD LOGIC
        previousLongestRoadPlayer = newState.playerDataList[newState.longestRoad[0]] if newState.longestRoad[0] != -1 else None
        previousLongestRoadLength = newState.longestRoad[1]

        exploredEdges = [self.edgeID]
        maxLength = self.exploreLongestRoadNode(newState.board, newEdge.nodeOne, 1, exploredEdges, playerData.color)
        maxLength += self.exploreLongestRoadNode(newState.board, newEdge.nodeTwo, 0, exploredEdges, playerData.color)

        if maxLength > 4 and maxLength > previousLongestRoadLength :
            if not previousLongestRoadPlayer == None :
                previousLongestRoadPlayer.victoryPoints -= 2
            playerData.victoryPoints += 2
            newState.longestRoad = (newState.whoseTurn, maxLength)

        return newState

    def exploreLongestRoadNode(self, board, nodeID, currentLength, exploredEdges, playerColor) :
        node = board.nodes[nodeID]
        for edgeID in node.edges :
            if not edgeID in exploredEdges :
                edge = board.edges[edgeID]
                exploredEdges.append(edgeID)
                if edge.playerColor == playerColor :
                    if edge.nodeOne == nodeID :
                        currentLength = max(currentLength, self.exploreLongestRoadNode(board, edge.nodeTwo, currentLength + 1, exploredEdges, playerColor))
                    else :
                        currentLength = max(currentLength, self.exploreLongestRoadNode(board, edge.nodeOne, currentLength + 1, exploredEdges, playerColor))
        
        return currentLength

    def getActionAsString(self):
        return "BuildRoad on " + str('%02d' % self.edgeID)
