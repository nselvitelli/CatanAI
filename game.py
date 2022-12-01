import pygame


DEBUG_STATES = True


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
        exit_gui = False
        game_over_printed_once = False

        if not self.display == None:
            self.display.initialize(self.state)

        nextState = self.state
        prevState = self.state

        while not exit_gui:
            if not self.display == None:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_gui = True

            if nextState.isGameOver():
                if not game_over_printed_once:
                    print("GAME OVER")
                    print("WINNER: ", nextState.getWinner().color)
                    game_over_printed_once = True
                    if not DEBUG_STATES:
                        nextState.printStateDifferences(prevState)
            else:
                currentPlayerData = self.state.playerDataList[self.state.whoseTurn]
                currentAgent = currentPlayerData.agent

                action = currentAgent.getAction(self.state)
                if DEBUG_STATES:
                    action.debug = True # print debug only when it is an official game move

                prevState = nextState
                nextState = action.apply(self.state)
                if DEBUG_STATES:
                    nextState.printStateDifferences(prevState)

            self.state = nextState
            if not self.display == None:
                self.display.drawState(self.state)
