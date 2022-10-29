
import random
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
    def __init__(self) -> None:
        
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
        self.tiles['J'] = Tile(-1, Resource.DESERT, [20, 21, 22, 31, 32, 33]) # Desert
        self.tiles['K'] = Tile(frequency_pool[9], resource_pool[9], [22, 23, 24, 33, 34, 35])
        self.tiles['L'] = Tile(frequency_pool[10], resource_pool[10], [24, 25, 26, 35, 36, 37])
        self.tiles['M'] = Tile(frequency_pool[11], resource_pool[11], [28, 29, 30, 38, 39, 40])
        self.tiles['N'] = Tile(frequency_pool[12], resource_pool[12], [30, 31, 32, 40, 41, 42])
        self.tiles['O'] = Tile(frequency_pool[13], resource_pool[13], [32, 33, 34, 42, 43, 44])
        self.tiles['P'] = Tile(frequency_pool[14], resource_pool[14], [34, 35, 36, 44, 45, 46])
        self.tiles['Q'] = Tile(frequency_pool[15], resource_pool[15], [39, 40, 41, 47, 48, 49])
        self.tiles['R'] = Tile(frequency_pool[16], resource_pool[16], [41, 42, 43, 49, 50, 51])
        self.tiles['S'] = Tile(frequency_pool[17], resource_pool[17], [43, 44, 45, 51, 52, 53])
