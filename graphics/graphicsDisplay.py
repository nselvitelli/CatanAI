from graphics.graphicsUtils import *

DEFAULT_GRID_SIZE = 50.0
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
BACKGROUND_COLOR = formatColor(1, 1, 1)
TILE_SHAPE = [
    (0.25, 0),
    (0.75, 0),
    (0.25, 1),
    (0.75, 1),
    (0, 0.5),
    (1, 0.5),
]
TILE_SIZE = 0.65


class CatanGraphics:
    def __init__(self, zoom=1.0):
        self.zoom = zoom
        self.gridSize = DEFAULT_GRID_SIZE * zoom

    def initialize(self, state):
        self.startGraphics(state)
        self.drawState(state)

    def startGraphics(self, state):
        self.width = 20
        self.height = 11
        self.make_window(self.width, self.height)

    def finish(self):
        end_graphics()

    def make_window(self, width, height):
        grid_width = (width-1) * self.gridSize
        grid_height = (height-1) * self.gridSize
        screen_width = 2*self.gridSize + grid_width
        screen_height = 2*self.gridSize + grid_height

        begin_graphics(screen_width,
                       screen_height,
                       BACKGROUND_COLOR,
                       "Catan")

    def to_screen(self, point):
        print(self.height)
        (x, y) = point
        #y = self.height - y
        x = (x + 1)*self.gridSize
        y = (self.height - y)*self.gridSize
        return (x, y)

    def drawState(self, state):
        # self.drawboard()
        self.drawTile(None, (11, 5))
        refresh()

    def drawTile(self, tile, topLeft):
        (screen_x, screen_y) = (self.to_screen(topLeft))
        print(screen_y)
        #coords = []
        # for (x, y) in TILE_SHAPE:
        #   coords.append((x*self.gridSize*TILE_SIZE + screen_x,
        #                   y*self.gridSize*TILE_SIZE + screen_y))
        # print(coords)
        coords = [(360.0, 185.85), (364.875, 194.625), (369.75, 185.85), (374.625, 194.625), (374.625, 170.25), (369.75,
                                                                                                                 165.375), (350.25, 165.375), (345.375, 170.25), (345.375, 194.625), (350.25, 185.85), (355.125, 194.625)]
        colour = formatColor(0, 0, 0)
        body = polygon(coords, colour, filled=1)
