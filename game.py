import time
import pygame


class Game:
    """
    The Game manages the control flow, soliciting actions from agents.
    """

    def __init__(self, display, state):
        self.display = display
        self.state = state

    def run(self):
        """
        Main control loop for game play.
        """
        exit = False

        self.display.initialize(self.state)

        while not exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit = True
            pygame.display.update()
