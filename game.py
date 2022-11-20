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
        if not self.display == None:
            self.display.initialize(self.state)

        nextState = self.state

        while not exit:
            if not self.display == None:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit = True

            if(nextState.isGameOver()):
                print("GAME OVER")
                print("WINNER: ", nextState.getWinner().color)
                # exit = True
            else:
                currentPlayerData = self.state.playerDataList[self.state.whoseTurn]
                currentAgent = currentPlayerData.agent
                action = currentAgent.getAction(self.state)
                nextState = action.apply(self.state)

            self.state = nextState
            if not self.display == None:
                self.display.drawState(self.state)
