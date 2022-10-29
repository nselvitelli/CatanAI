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

    def getTreeEndpoints(self, playerColor):
        self.getTreeEndpointsWithExplored(playerColor, [])

    def getTreeEndpointsWithExplored(self, playerColor, explored):
        pass


class Edge:

    def __init__(self) -> None:
        self.playerColor = PlayerColor.BLANK
        

class NodePiece(Enum):
    EMPTY = 0
    SETTLEMENT = 1
    CITY = 2

    def __init__(self) -> None:
        super().__init__()