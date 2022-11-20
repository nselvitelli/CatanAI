from enum import Enum

from PlayerData import PlayerColor


class NodePiece(Enum):
    EMPTY = 0
    SETTLEMENT = 1
    CITY = 2


class Port(Enum):
    EMPTY = 0
    BRICK = 1
    WHEAT = 2
    SHEEP = 3
    ORE = 4
    LOG = 5
    THREE_TO_ONE = 6


class Node:

    def __init__(self, edges, id, piece=(NodePiece.EMPTY, PlayerColor.BLANK), port=Port.EMPTY) -> None:
        self.piece = piece  # tuple of type and color
        self.port = port
        self.edges = edges
        self.id = id

    def bfsEndpoints(self, playerColor, explored, edgeMap, nodeMap):
        if self.id in explored:
            return []

        endpoints = []
        for edge in self.edges:
            endpoints.extend(edgeMap[edge].bfsEndpoints(
                playerColor, (explored + [self.id]), self.id, nodeMap, edgeMap))
        return endpoints

    def bfsPossibleSettlements(self, playerColor, explored, edgeMap, nodeMap):
        if self.id in explored:
            return []

        if self.piece == (NodePiece.EMPTY, PlayerColor.BLANK):
            for edge in self.edges:
                if edge.adjacentSettlement(self.id, nodeMap, edgeMap):
                    return []
            return [self.id]

        possibles = []
        for edge in self.edges:
            print(edge, edgeMap)
            possibles.extend(edgeMap[edge].bfsPossibleSettlements(
                self, playerColor, explored, nodeMap, edgeMap))
        return possibles

    # def bfsUpgradeableSettlements(self, playerColor, explored, edgeMap, nodeMap):
    #     if self.id in explored:
    #         return []

    #     if self.piece == (NodePiece.SETTLEMENT, playerColor):
    #         return [self.id]

    #     possibles = []
    #     for edge in self.edges:
    #         possibles.extend(edgeMap[edge].bfsUpgradeableSettlements(
    #             self, playerColor, explored, edgeMap, nodeMap))
    #     return possibles

    def getCopy(self):
        newEdges = []
        for edge in self.edges:
            newEdges.append(edge)
        return Node(newEdges, self.id, self.piece, self.port)


class Edge:

    def __init__(self, id, nodeOne, nodeTwo, playerColor=PlayerColor.BLANK) -> None:
        self.playerColor = playerColor
        self.id = id
        self.nodeOne = nodeOne
        self.nodeTwo = nodeTwo

    def bfsEndpoints(self, playerColor, explored, comingFrom, nodeMap, edgeMap):
        if self.playerColor == PlayerColor.BLANK:
            return [self.id]
        elif self.playerColor == playerColor:
            otherNode = self.nodeOne if self.nodeTwo == comingFrom else self.nodeTwo
            return nodeMap[otherNode].bfsEndpoints(playerColor, explored, edgeMap, nodeMap)
        else:
            return []

    def bfsPossibleSettlements(self, playerColor, explored, comingFrom, nodeMap, edgeMap):
        if self.playerColor == playerColor:
            otherNode = self.nodeOne if self.nodeTwo == comingFrom else self.nodeTwo
            return nodeMap[otherNode].bfsPossibleSettlements(playerColor, explored, edgeMap, nodeMap)
        else:
            return []

    def adjacentSettlement(self, comingFrom, nodeMap, edgeMap):
        otherNode = self.nodeOne if self.nodeTwo == comingFrom else self.nodeTwo
        return nodeMap[otherNode].piece[0] != NodePiece.EMPTY

    # def bfsUpgradeableSettlements(self, playerColor, explored, comingFrom, nodeMap, edgeMap):
    #     if self.playerColor == playerColor:
    #         otherNode = self.nodeOne if self.nodeTwo == comingFrom else self.nodeTwo
    #         return nodeMap[otherNode].bfsUpgradeableSettlements(playerColor, explored, nodeMap, edgeMap)
    #     else:
    #         return []

    def getCopy(self):
        return Edge(self.id, self.nodeOne, self.nodeTwo, self.playerColor)
