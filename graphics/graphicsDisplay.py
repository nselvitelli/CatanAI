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


class CatanGraphics:
    def __init__(self, zoom=1.0):
        self.zoom = zoom
        self.gridSize = DEFAULT_GRID_SIZE * zoom

    def initialize(self, state):
        pygame.init()

        self.canvas = pygame.display.set_mode((800, 800))
        # TITLE OF CANVAS
        pygame.display.set_caption("Catan")
        self.canvas.fill(WHITE)

        self.drawState(state)

    def drawState(self, state):
        startX = 250
        startY = 100
        yOffset = TILE_SIZE * math.sqrt(3) / 2

        (x, y) = (startX, startY)
        # draw row 1:
        self.drawTile(None, (x, y))
        x += TILE_SIZE
        self.drawTile(None, (x, y))
        x += TILE_SIZE
        self.drawTile(None, (x, y))
        # draw row 2:
        x = startX - TILE_SIZE / 2
        y = startY + yOffset
        self.drawTile(None, (x, y))
        #self.drawTile(state.board.tiles['A'], pos)
        #self.drawTile(state.board.tiles['B'], pos2)
        pygame.display.update()

    def drawTile(self, tile, pos):

        coords = []
        for (x, y) in TILE_SHAPE:
            newPos = (TILE_SIZE * x + pos[0], TILE_SIZE * y + pos[1])
            coords.append(newPos)

        color = rect_color  # TILE_COLOR_MAP[tile.resource]
        pygame.draw.polygon(self.canvas, color, coords)
