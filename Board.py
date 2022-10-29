
import random
from Node import Node, NodePiece
from PlayerData import PlayerColor
from Resource import Resource
from Tile import Tile


class Board:

    def __init__(self, tiles, nodes, edges, robber_tile) -> None:
        self.tiles = tiles
        self.nodes = nodes
        self.edges = edges
        self.robber_tile = robber_tile


    """
    BOARD HARDCODE
    """
    def generate_start_board(self) -> None:
        
        resource_pool = [
            Resource.BRICK, Resource.BRICK, Resource.BRICK,
            Resource.SHEEP, Resource.SHEEP, Resource.SHEEP, Resource.SHEEP,
            Resource.LOG, Resource.LOG, Resource.LOG, Resource.LOG,
            Resource.WHEAT, Resource.WHEAT, Resource.WHEAT, Resource.WHEAT,
            Resource.ORE, Resource.ORE, Resource.ORE
        ]
        random.shuffle(resource_pool)

        frequency_pool = [
            2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12
        ]
        random.shuffle(frequency_pool)

        self.nodes = []
        self.edges = []

        self.robber_tile = 'J'

        self.tiles = {}
        self.tiles['A'] = Tile(frequency_pool[0], resource_pool[0], [0, 1, 2, 8, 9, 10])
        self.tiles['B'] = Tile(frequency_pool[1], resource_pool[1], [2, 3, 4, 10, 11, 12])
        self.tiles['C'] = Tile(frequency_pool[2], resource_pool[2], [4, 5, 6, 12, 13, 14])
        self.tiles['D'] = Tile(frequency_pool[3], resource_pool[3], [7, 8, 9, 17, 18, 19])
        self.tiles['E'] = Tile(frequency_pool[4], resource_pool[4], [9, 10, 11, 19, 20, 21])
        self.tiles['F'] = Tile(frequency_pool[5], resource_pool[5], [11, 12, 14, 21, 22, 23])
        self.tiles['G'] = Tile(frequency_pool[6], resource_pool[6], [13, 14, 15, 23, 24, 25])
        self.tiles['H'] = Tile(frequency_pool[7], resource_pool[7], [16, 17, 18, 27, 28, 29])
        self.tiles['I'] = Tile(frequency_pool[8], resource_pool[8], [18, 19, 20, 29, 30, 31])
        self.tiles['J'] = Tile(-1, Resource.DESERT, [20, 21, 22, 31, 32, 33]) # Always Desert
        self.tiles['K'] = Tile(frequency_pool[9], resource_pool[9], [22, 23, 24, 33, 34, 35])
        self.tiles['L'] = Tile(frequency_pool[10], resource_pool[10], [24, 25, 26, 35, 36, 37])
        self.tiles['M'] = Tile(frequency_pool[11], resource_pool[11], [28, 29, 30, 38, 39, 40])
        self.tiles['N'] = Tile(frequency_pool[12], resource_pool[12], [30, 31, 32, 40, 41, 42])
        self.tiles['O'] = Tile(frequency_pool[13], resource_pool[13], [32, 33, 34, 42, 43, 44])
        self.tiles['P'] = Tile(frequency_pool[14], resource_pool[14], [34, 35, 36, 44, 45, 46])
        self.tiles['Q'] = Tile(frequency_pool[15], resource_pool[15], [39, 40, 41, 47, 48, 49])
        self.tiles['R'] = Tile(frequency_pool[16], resource_pool[16], [41, 42, 43, 49, 50, 51])
        self.tiles['S'] = Tile(frequency_pool[17], resource_pool[17], [43, 44, 45, 51, 52, 53])

        self.nodes[0] = Node([0, 6], 0, (NodePiece.EMPTY, PlayerColor.BLANK))    # v
        self.nodes[1] = Node([0, 1], 1, (NodePiece.EMPTY, PlayerColor.BLANK))    # ^
        self.nodes[2] = Node([1, 2, 7],2, (NodePiece.EMPTY, PlayerColor.BLANK)) # v
        self.nodes[3] = Node([2, 3], 3, (NodePiece.EMPTY, PlayerColor.BLANK))    # ^
        self.nodes[4] = Node([3, 4, 8], 4, (NodePiece.EMPTY, PlayerColor.BLANK)) # v
        self.nodes[5] = Node([4, 5], 5, (NodePiece.EMPTY, PlayerColor.BLANK))    # ^
        self.nodes[6] = Node([5, 9], 6, (NodePiece.EMPTY, PlayerColor.BLANK))    # v

        self.nodes[7] = Node([10, 18], 7, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[8] = Node([10, 11, 6], 8, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[9] = Node([11, 12, 19], 9, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[10] = Node([12, 13, 7], 10, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[11] = Node([13, 14, 20], 11, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[12] = Node([14, 15, 8], 12, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[13] = Node([15, 16, 21], 13, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[14] = Node([16, 17, 9], 14, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[15] = Node([17, 22], 15, (NodePiece.EMPTY, PlayerColor.BLANK))

        self.nodes[16] = Node([23, 33], 16, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[17] = Node([23, 24, 18], 17, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[18] = Node([24, 25, 34], 18, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[19] = Node([25, 26, 19], 19, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[20] = Node([26, 27, 35], 20, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[21] = Node([27, 28, 20], 21, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[22] = Node([28, 29, 36], 22, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[23] = Node([29, 30, 21], 23, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[24] = Node([30, 31, 37], 24, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[25] = Node([31, 32, 22], 25, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[26] = Node([32, 38], 26, (NodePiece.EMPTY, PlayerColor.BLANK))

        self.nodes[27] = Node([39, 33], 27, (NodePiece.EMPTY, PlayerColor.BLANK)) # ^
        self.nodes[28] = Node([39, 40, 49], 28, (NodePiece.EMPTY, PlayerColor.BLANK)) # v
        self.nodes[29] = Node([40, 41, 34], 29, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[30] = Node([41, 42, 50], 30, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[31] = Node([42, 43, 35], 31, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[32] = Node([43, 44, 51], 32, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[33] = Node([44, 45, 36], 33, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[34] = Node([45, 46, 52], 34, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[35] = Node([46, 47, 37], 35, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[36] = Node([47, 48, 53], 36, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[37] = Node([41, 42, 38], 37, (NodePiece.EMPTY, PlayerColor.BLANK))

        self.nodes[38] = Node([54, 49], 38, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[39] = Node([54, 55, 62], 39, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[40] = Node([55, 56, 50], 40, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[41] = Node([56, 57, 63], 41, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[42] = Node([57, 58, 51], 42, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[43] = Node([58, 59, 64], 43, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[44] = Node([59, 60, 52], 44, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[45] = Node([60, 61, 65], 45, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[46] = Node([61, 53], 46, (NodePiece.EMPTY, PlayerColor.BLANK))

        self.nodes[47] = Node([66, 62], 47, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[48] = Node([66, 67], 48, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[49] = Node([67, 68, 63], 49, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[50] = Node([68, 69], 50, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[51] = Node([69, 70, 64], 51, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[52] = Node([70, 71], 52, (NodePiece.EMPTY, PlayerColor.BLANK))
        self.nodes[53] = Node([71, 65], 53, (NodePiece.EMPTY, PlayerColor.BLANK))

        self.edges[0] = 
