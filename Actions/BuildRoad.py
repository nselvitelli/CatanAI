from hashlib import new
from Actions.Action import Action
from Board import Board
from Node import Edge


# NOT DONE
class BuildRoad(Action):

    def __init__(self, edgeID) -> None:
        super().__init__()
        self.edgeID = edgeID

    def apply(self, state):
        newEdges = {}
        for edgeID in state.board.edges:
            if edgeID == self.edgeID:
                newEdges[edgeID] = Edge(
                    edgeID, state.board.edges[edgeID].nodeOne, state.board.edges[edgeID].nodeTwo, state.whoseTurn)
            else:
                newEdges[edgeID] = Edge(
                    edgeID, state.board.edges[edgeID].nodeOne, state.board.edges[edgeID].nodeTwo, state.board.edges[edgeID].playerColor)
        board = Board(state.board.tiles, state.board.nodes,
                      state.board.edges, self.tileID)
