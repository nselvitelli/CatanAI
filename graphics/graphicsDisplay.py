import pygame

rect_color = (255, 0, 0)

DEFAULT_GRID_SIZE = 50.0
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
TILE_SHAPE = [
    (0, 0.5),
    (0.25, 0),
    (0.75, 0),
    (1, 0.5),
    (0.75, 1),
    (0.25, 1),
]
TILE_SIZE = 50

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

        pos = (5, 5)
        self.drawTile(None, pos)
        pygame.display.update()

    def drawTile(self, state, pos):
        coords = []
        for (x, y) in TILE_SHAPE:
            newPos = (TILE_SIZE * (x + pos[0]), TILE_SIZE * (y + pos[1]))
            coords.append(newPos)

        color = rect_color
        pygame.draw.polygon(self.canvas, color, coords)
