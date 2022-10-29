
import random
from typing_extensions import Self
from Node import Edge, Node, NodePiece
from PlayerData import PlayerColor
from Resource import Resource
from Tile import Tile


class Board:

    def __init__(self, tiles, nodes, edges, robber_tile) -> None:
        self.tiles = tiles
        self.nodes = nodes
        self.edges = edges
        self.robber_tile = robber_tile


    def getCopy(self) -> Self:
        tiles = {}
        for key in self.tiles.keys():
            tiles[key] = self.tiles[key].getCopy()
        nodes = {}
        for key in self.nodes.keys():
            nodes[key] = self.nodes[key].getCopy()
        edges = {}
        for key in self.edges.keys():
            edges[key] = self.edges[key].getCopy()
        return Board(tiles, nodes, edges, self.robber_tile)

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

        self.nodes = {}
        self.edges = {}

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
        self.nodes[37] = Node([48, 38], 37, (NodePiece.EMPTY, PlayerColor.BLANK))

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

        self.edges[ 0 ] = Edge( 0 , 0 , 1 )
        self.edges[ 1 ] = Edge( 1 , 1 , 2 )
        self.edges[ 2 ] = Edge( 2 , 2 , 3 )
        self.edges[ 3 ] = Edge( 3 , 3 , 4 )
        self.edges[ 4 ] = Edge( 4 , 4 , 5 )
        self.edges[ 5 ] = Edge( 5 , 5 , 6 )
        self.edges[ 6 ] = Edge( 6 , 0 , 8 )
        self.edges[ 7 ] = Edge( 7 , 2 , 10 )
        self.edges[ 8 ] = Edge( 8 , 4 , 12 )
        self.edges[ 9 ] = Edge( 9 , 6 , 14 )
        self.edges[ 10 ] = Edge( 10 , 7 , 8 )
        self.edges[ 11 ] = Edge( 11 , 8 , 9 )
        self.edges[ 12 ] = Edge( 12 , 9 , 10 )
        self.edges[ 13 ] = Edge( 13 , 10 , 11 )
        self.edges[ 14 ] = Edge( 14 , 11 , 12 )
        self.edges[ 15 ] = Edge( 15 , 12 , 13 )
        self.edges[ 16 ] = Edge( 16 , 13 , 14 )
        self.edges[ 17 ] = Edge( 17 , 14 , 15 )
        self.edges[ 18 ] = Edge( 18 , 7 , 17 )
        self.edges[ 19 ] = Edge( 19 , 9 , 19 )
        self.edges[ 20 ] = Edge( 20 , 11 , 21 )
        self.edges[ 21 ] = Edge( 21 , 13 , 23 )
        self.edges[ 22 ] = Edge( 22 , 15 , 25 )
        self.edges[ 23 ] = Edge( 23 , 16 , 17 )
        self.edges[ 24 ] = Edge( 24 , 17 , 18 )
        self.edges[ 25 ] = Edge( 25 , 18 , 19 )
        self.edges[ 26 ] = Edge( 26 , 19 , 20 )
        self.edges[ 27 ] = Edge( 27 , 20 , 21 )
        self.edges[ 28 ] = Edge( 28 , 21 , 22 )
        self.edges[ 29 ] = Edge( 29 , 22 , 23 )
        self.edges[ 30 ] = Edge( 30 , 23 , 24 )
        self.edges[ 31 ] = Edge( 31 , 24 , 25 )
        self.edges[ 32 ] = Edge( 32 , 25 , 26 )
        self.edges[ 33 ] = Edge( 33 , 16 , 27 )
        self.edges[ 34 ] = Edge( 34 , 18 , 29 )
        self.edges[ 35 ] = Edge( 35 , 20 , 31 )
        self.edges[ 36 ] = Edge( 36 , 22 , 33 )
        self.edges[ 37 ] = Edge( 37 , 24 , 35 )
        self.edges[ 38 ] = Edge( 38 , 26 , 37 )
        self.edges[ 39 ] = Edge( 39 , 27 , 28 )
        self.edges[ 40 ] = Edge( 40 , 28 , 29 )
        self.edges[ 41 ] = Edge( 41 , 29 , 30 )
        self.edges[ 42 ] = Edge( 42 , 30 , 31 )
        self.edges[ 43 ] = Edge( 43 , 31 , 32 )
        self.edges[ 44 ] = Edge( 44 , 32 , 33 )
        self.edges[ 45 ] = Edge( 45 , 33 , 34 )
        self.edges[ 46 ] = Edge( 46 , 34 , 35 )
        self.edges[ 47 ] = Edge( 47 , 35 , 36 )
        self.edges[ 48 ] = Edge( 48 , 36 , 37 )
        self.edges[ 49 ] = Edge( 49 , 28 , 38 )
        self.edges[ 50 ] = Edge( 50 , 30 , 40 )
        self.edges[ 51 ] = Edge( 51 , 32 , 42 )
        self.edges[ 52 ] = Edge( 52 , 34 , 44 )
        self.edges[ 53 ] = Edge( 53 , 36 , 46 )
        self.edges[ 54 ] = Edge( 54 , 38 , 39 )
        self.edges[ 55 ] = Edge( 55 , 39 , 40 )
        self.edges[ 56 ] = Edge( 56 , 40 , 41 )
        self.edges[ 57 ] = Edge( 57 , 41 , 42 )
        self.edges[ 58 ] = Edge( 58 , 42 , 43 )
        self.edges[ 59 ] = Edge( 59 , 43 , 44 )
        self.edges[ 60 ] = Edge( 60 , 44 , 45 )
        self.edges[ 61 ] = Edge( 61 , 45 , 46 )
        self.edges[ 62 ] = Edge( 62 , 39 , 47 )
        self.edges[ 63 ] = Edge( 63 , 41 , 49 )
        self.edges[ 64 ] = Edge( 64 , 43 , 51 )
        self.edges[ 65 ] = Edge( 65 , 45 , 53 )
        self.edges[ 66 ] = Edge( 66 , 47 , 48 )
        self.edges[ 67 ] = Edge( 67 , 48 , 49 )
        self.edges[ 68 ] = Edge( 68 , 49 , 50 )
        self.edges[ 69 ] = Edge( 69 , 50 , 51 )
        self.edges[ 70 ] = Edge( 70 , 51 , 52 )
        self.edges[ 71 ] = Edge( 71 , 52 , 53 )