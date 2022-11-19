from graphics.graphicsUtils import *

DEFAULT_GRID_SIZE = 50.0
WINDOW_WIDTH = 10000
WINDOW_HEIGHT = 10000
BACKGROUND_COLOR = formatColor(1, 1, 1)
TILE_SHAPE = [
    (0.25, 0),
    (0.75, 0),
    (0.25, 1),
    (0.75, 1),
    (0, 0.5),
    (1, 0.5),
]


class CatanGraphics:
    def __init__(self, zoom=1.0):
        self.zoom = zoom
        self.gridSize = DEFAULT_GRID_SIZE * zoom

    def initialize(self, state):
        self.startGraphics(state)
        self.drawState(state)

    def startGraphics(self, state):
        self.width = WINDOW_WIDTH
        self.height = WINDOW_HEIGHT
        self.make_window(WINDOW_WIDTH, WINDOW_HEIGHT)

    def make_window(self, width, height):
        screen_width = width
        screen_height = height

        begin_graphics(screen_width,
                       screen_height,
                       BACKGROUND_COLOR,
                       "Catan")

    def to_screen(self, point):
        (x, y) = point
        #y = self.height - y
        x = (x + 1)*self.gridSize
        y = (self.height - y)*self.gridSize
        return (x, y)

    def drawState(self, state):
        # self.drawboard()
        self.drawTile(None, None)
        refresh()

    def drawTile(self, tile, topLeft):
        (screen_x, screen_y) = (1, 1)  # (self.to_screen(topLeft))
        coords = []
        for (x, y) in TILE_SHAPE:
            coords.append((x + screen_x,
                           y + screen_y))
        print(coords)
        colour = formatColor(1, 1, 1)
        body = polygon(coords, colour, filled=1)
