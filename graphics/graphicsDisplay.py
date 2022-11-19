import pygame
import math
from Resource import Resource

TILE_COLOR_MAP = {
    Resource.DESERT: (255, 255, 204),
    Resource.BRICK: (255, 51, 51),
    Resource.WHEAT: (255, 255, 0),
    Resource.SHEEP: (178, 255, 102),
    Resource.ORE: (96, 96, 96),
    Resource.LOG: (0, 102, 0)
}

rect_color = (255, 0, 0)

DEFAULT_GRID_SIZE = 50.0
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
TILE_SHAPE = [
    (.5, 0),
    (0, 0.25),
    (0, 0.75),
    (0.5, 1),
    (1, 0.75),
    (1, 0.25),
]
TILE_SIZE = 80

WHITE = (255, 255, 255)
GREY = (211, 211, 211)


class CatanGraphics:
    def __init__(self, zoom=1.0):
        self.zoom = zoom
        self.gridSize = DEFAULT_GRID_SIZE * zoom

    def initialize(self, state):
        pygame.init()
        pygame.font.init()

        self.canvas = pygame.display.set_mode((800, 800))
        # TITLE OF CANVAS
        pygame.display.set_caption("Catan")
        self.canvas.fill(WHITE)

        self.drawState(state)

    def drawState(self, state):
        self.drawBoard(state.board)
        pygame.display.update()

    def drawBoard(self, board):
        startX = 250
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
