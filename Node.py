from enum import Enum

from PlayerData import PlayerColor

class Node:

    def __init__(self, edges, tiles, piece, id) -> None:
        self.piece = piece # tuple of type and color
        self.edges = edges
        self.tiles = tiles
        self.id = id

    def __init__(self, edges, tiles, id) -> None:
        self.__init__(edges, tiles, (NodePiece.EMPTY, PlayerColor.BLANK), id)

    def bfsEndpoints(self, playerColor, explored, edgeMap, nodeMap):
        if self.id in explored:
            return []

        endpoints = []
        for edge in self.edges:
            endpoints.extend(edgeMap[edge].bfsEndpoints(playerColor, explored + [self.id], self.id, edgeMap, nodeMap))
        return endpoints


class Edge:

    def __init__(self, playerColor, id, nodeOneID, nodeTwoID) -> None:
        self.playerColor = playerColor
        self.id = id

    def __init__(self, nodeOne, nodeTwo) -> None:
        self.__init__(PlayerColor.BLANK, nodeOne, nodeTwo)

    def bfsEndpoints(self, playerColor, explored, comingFrom, nodeMap, edgeMap):
        if self.playerColor == PlayerColor.BLANK:
            return [self.id]
        elif self.playerColor == playerColor:
            otherNode = self.id-comingFrom
            return nodeMap[otherNode].bfsEndpoints(playerColor, explored, nodeMap, edgeMap)
        else:
            return []


        

class NodePiece(Enum):
    EMPTY = 0
    SETTLEMENT = 1
    CITY = 2

    def __init__(self) -> None:
        super().__init__()