import pygame
import math
from Resource import Resource
from PlayerColor import PlayerColor
from Node import NodePiece, Port


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (211, 211, 211)

TILE_COLOR_MAP = {
    Resource.DESERT: (255, 255, 204),
    Resource.BRICK: (255, 102, 102),
    Resource.WHEAT: (255, 255, 0),
    Resource.SHEEP: (178, 255, 102),
    Resource.ORE: (96, 96, 96),
    Resource.LOG: (0, 102, 0)
}

PLAYER_COLOR_MAP = {
    PlayerColor.BLUE: (0, 0, 255),
    PlayerColor.ORANGE: (255, 128, 0),
    PlayerColor.RED: (255, 0, 0),
    PlayerColor.WHITE: WHITE
}

PORT_COLOR_MAP = {
    Port.BRICK: TILE_COLOR_MAP[Resource.BRICK],
    Port.LOG: TILE_COLOR_MAP[Resource.LOG],
    Port.ORE: TILE_COLOR_MAP[Resource.ORE],
    Port.SHEEP: TILE_COLOR_MAP[Resource.SHEEP],
    Port.THREE_TO_ONE: TILE_COLOR_MAP[Resource.DESERT],
    Port.WHEAT: TILE_COLOR_MAP[Resource.WHEAT]
}

TILE_SHAPE = [
    (.5, 0),
    (0, 0.25),
    (0, 0.75),
    (0.5, 1),
    (1, 0.75),
    (1, 0.25),
]
TILE_SIZE = 80

SETTLEMENT_SHAPE = [
    (0, 0),
    (0, 1),
    (1, 1),
    (1, 0)
]
SETTLEMENT_SIZE = 10

CITY_SHAPE = [
    (0.5, 0),
    (1, 1),
    (0, 1)
]
CITY_SIZE = 10


class CatanGraphics:
    def __init__(self, zoom=1.0):
        self.zoom = zoom

    def initialize(self, state):
        pygame.init()
        pygame.font.init()

        self.canvas = pygame.display.set_mode((600, 600))
        # TITLE OF CANVAS
        pygame.display.set_caption("Catan")
        self.canvas.fill(BLACK)

        self.drawState(state)

    def drawState(self, state):
        self.canvas.fill(BLACK)
        self.drawBoard(state.board)
        pygame.display.update()

    def drawBoard(self, board):
        startX = 150
        startY = 100
        yOffset = TILE_SIZE * math.sqrt(2.5) / 2

        (x, y) = (startX, startY)
        # draw row 1:
        self.drawTile(board, 'A', (x, y))
        x += TILE_SIZE
        self.drawTile(board, 'B', (x, y))
        x += TILE_SIZE
        self.drawTile(board, 'C', (x, y))
        # draw row 2:
        x = startX - TILE_SIZE / 2
        y = startY + yOffset
        self.drawTile(board, 'D', (x, y))
        x += TILE_SIZE
        self.drawTile(board, 'E', (x, y))
        x += TILE_SIZE
        self.drawTile(board, 'F', (x, y))
        x += TILE_SIZE
        self.drawTile(board, 'G', (x, y))
        # draw row 3
        x = startX - TILE_SIZE
        y = startY + 2 * yOffset
        self.drawTile(board, 'H', (x, y))
        x += TILE_SIZE
        self.drawTile(board, 'I', (x, y))
        x += TILE_SIZE
        self.drawTile(board, 'J', (x, y))
        x += TILE_SIZE
        self.drawTile(board, 'K', (x, y))
        x += TILE_SIZE
        self.drawTile(board, 'L', (x, y))
        # draw row 4:
        x = startX - TILE_SIZE / 2
        y = startY + 3 * yOffset
        self.drawTile(board, 'M', (x, y))
        x += TILE_SIZE
        self.drawTile(board, 'N', (x, y))
        x += TILE_SIZE
        self.drawTile(board, 'O', (x, y))
        x += TILE_SIZE
        self.drawTile(board, 'P', (x, y))
        # draw row 5:
        x = startX
        y = startY + 4 * yOffset
        self.drawTile(board, 'Q', (x, y))
        x += TILE_SIZE
        self.drawTile(board, 'R', (x, y))
        x += TILE_SIZE
        self.drawTile(board, 'S', (x, y))

        self.drawNodes(board)

    def drawNodes(self, board):
        startX = 150
        startY = 100
        yOffset = TILE_SIZE * math.sqrt(2.5) / 2

        (x, y) = (startX, startY)
        # draw row 1:
        self.drawNodesFromTile(board, board.tiles['A'], (x, y))
        x += TILE_SIZE
        self.drawNodesFromTile(board, board.tiles['B'], (x, y))
        x += TILE_SIZE
        self.drawNodesFromTile(board, board.tiles['C'], (x, y))
        # draw row 2:
        x = startX - TILE_SIZE / 2
        y = startY + yOffset
        self.drawNodesFromTile(board, board.tiles['D'], (x, y))
        x += TILE_SIZE
        self.drawNodesFromTile(board, board.tiles['E'], (x, y))
        x += TILE_SIZE
        self.drawNodesFromTile(board, board.tiles['F'], (x, y))
        x += TILE_SIZE
        self.drawNodesFromTile(board, board.tiles['G'], (x, y))
        # draw row 3
        x = startX - TILE_SIZE
        y = startY + 2 * yOffset
        self.drawNodesFromTile(board, board.tiles['H'], (x, y))
        x += TILE_SIZE
        self.drawNodesFromTile(board, board.tiles['I'], (x, y))
        x += TILE_SIZE
        self.drawNodesFromTile(board, board.tiles['J'], (x, y))
        x += TILE_SIZE
        self.drawNodesFromTile(board, board.tiles['K'], (x, y))
        x += TILE_SIZE
        self.drawNodesFromTile(board, board.tiles['L'], (x, y))
        # draw row 4:
        x = startX - TILE_SIZE / 2
        y = startY + 3 * yOffset
        self.drawNodesFromTile(board, board.tiles['M'], (x, y))
        x += TILE_SIZE
        self.drawNodesFromTile(board, board.tiles['N'], (x, y))
        x += TILE_SIZE
        self.drawNodesFromTile(board, board.tiles['O'], (x, y))
        x += TILE_SIZE
        self.drawNodesFromTile(board, board.tiles['P'], (x, y))
        # draw row 5:
        x = startX
        y = startY + 4 * yOffset
        self.drawNodesFromTile(board, board.tiles['Q'], (x, y))
        x += TILE_SIZE
        self.drawNodesFromTile(board, board.tiles['R'], (x, y))
        x += TILE_SIZE
        self.drawNodesFromTile(board, board.tiles['S'], (x, y))

    def drawTile(self, board, tileID, pos):
        tile = board.tiles[tileID]
        coords = []
        for (x, y) in TILE_SHAPE:
            newPos = (TILE_SIZE * x + pos[0], TILE_SIZE * y + pos[1])
            coords.append(newPos)

        color = TILE_COLOR_MAP[tile.resource]
        pygame.draw.polygon(self.canvas, color, coords)
        if board.robber_tile == tileID:
            robberPos = (pos[0] + TILE_SIZE / 2, pos[1] + TILE_SIZE / 2)
            pygame.draw.circle(self.canvas, GREY, robberPos, 10)
        elif tile.number > 0:
            my_font = pygame.font.SysFont('Comic Sans MS', 20)
            text_surface = my_font.render(str(tile.number), False, (0, 0, 0))
            textPos = (pos[0] + TILE_SIZE / 2.5, pos[1] + TILE_SIZE / 3)
            self.canvas.blit(text_surface, textPos)

        self.drawNodesFromTile(board, tile, pos)

    def drawNodesFromTile(self, board, tile, pos):
        self.drawEdges(board, tile, pos)
        # top left node:
        node = board.nodes[tile.nodes[0]]
        self.drawPiece(node, node.piece, pos, (0, 0.25))
        # top node:
        node = board.nodes[tile.nodes[1]]
        self.drawPiece(node, node.piece, pos, (0.5, 0))
        # top right node:
        node = board.nodes[tile.nodes[2]]
        self.drawPiece(node, node.piece, pos, (1, 0.25))
        # bottom left node:
        node = board.nodes[tile.nodes[3]]
        self.drawPiece(node, node.piece, pos, (0, 0.75))
        # bottom node:
        node = board.nodes[tile.nodes[4]]
        self.drawPiece(node, node.piece, pos, (0.5, 1))
        # bottom right node:
        node = board.nodes[tile.nodes[5]]
        self.drawPiece(node, node.piece, pos, (1, 0.75))

    def drawPiece(self, node, piece, pos, offset):
        newPos = (pos[0] + TILE_SIZE * offset[0] - SETTLEMENT_SIZE / 2,
                  pos[1] + TILE_SIZE * offset[1] - SETTLEMENT_SIZE / 2)
        if node.port != Port.EMPTY:
            pygame.draw.circle(self.canvas, PORT_COLOR_MAP[node.port], newPos, 8)
            pygame.draw.circle(self.canvas, BLACK, newPos, 8, width=1)
        
        if piece[0] == NodePiece.EMPTY:
            return
        coords = []
        if piece[0] == NodePiece.SETTLEMENT:
            for (x, y) in SETTLEMENT_SHAPE:
                coordPos = (SETTLEMENT_SIZE * x +
                            newPos[0], SETTLEMENT_SIZE * y + newPos[1])
                coords.append(coordPos)
        else:
            for (x, y) in CITY_SHAPE:
                coordPos = (CITY_SIZE * x +
                            newPos[0], CITY_SIZE * y + newPos[1])
                coords.append(newPos)
        pygame.draw.polygon(self.canvas, PLAYER_COLOR_MAP[piece[1]], coords)

    def drawEdges(self, board, tile, pos):
        self.drawEdge(board, tile.nodes[0],
                      tile.nodes[1], pos, (0, 0.25), (0.5, 0))
        self.drawEdge(board, tile.nodes[1],
                      tile.nodes[2], pos, (0.5, 0), (1, 0.25))

        self.drawEdge(board, tile.nodes[0],
                      tile.nodes[3], pos, (0, 0.25), (0, 0.75))
        self.drawEdge(board, tile.nodes[3],
                      tile.nodes[4], pos, (0, 0.75), (0.5, 1))
        self.drawEdge(board, tile.nodes[4],
                      tile.nodes[5], pos, (0.5, 1), (1, 0.75))
        self.drawEdge(board, tile.nodes[5],
                      tile.nodes[2], pos, (1, 0.75), (1, 0.25))

    def drawEdge(self, board, tileID1, tileID2, pos, offset1, offset2):
        for edgeID in board.edges:
            edge = board.edges[edgeID]
            if (edge.nodeOne == tileID1 and edge.nodeTwo == tileID2) or (edge.nodeOne == tileID2 and edge.nodeTwo == tileID1):
                if not edge.playerColor == PlayerColor.BLANK:
                    pos1 = (pos[0] + offset1[0] * TILE_SIZE,
                            pos[1] + offset1[1] * TILE_SIZE)
                    pos2 = (pos[0] + offset2[0] * TILE_SIZE,
                            pos[1] + offset2[1] * TILE_SIZE)
                    pygame.draw.line(
                        self.canvas, PLAYER_COLOR_MAP[edge.playerColor], pos1, pos2, 5)
    
    def drawText(self, message):
        fontSize = 64
        font = pygame.font.Font(None, fontSize)
        antialias = True
        textColor = (0, 255, 0)
        text = font.render("Pummel The Chimp, And Win $$$", antialias, textColor)
        textpos = text.get_rect(centerx=self.canvas.get_width() / 2, y=10)
        self.canvas.blit(text, textpos)
