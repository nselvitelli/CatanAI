from enum import Enum

from PlayerData import PlayerColor

class Node:

    def __init__(self, edges, tiles) -> None:
        self.piece = NodePiece.EMPTY
        self.edges = edges
        self.tiles = tiles


class Edge:

    def __init__(self) -> None:
        self.playerColor = PlayerColor.BLANK
        

class NodePiece(Enum):
    EMPTY = 0
    SETTLEMENT = 1
    CITY = 2

    def __init__(self) -> None:
        super().__init__()