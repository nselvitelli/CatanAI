import time

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
        # self.display.initialize(self.state)
        # time.sleep(0.5)
        while True:
            self.display.initialize(self.state)
            time.sleep(2)
            self.display.finish()
            time.sleep(2)

        # while not self.gameOver:
        # here is where we actually play game
