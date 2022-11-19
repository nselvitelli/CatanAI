import State
from game import Game
from graphics.graphicsDisplay import CatanGraphics


NUM_PLAYERS = 2  # TODO: take in as command line arg


if __name__ == '__main__':
    """
    The main function called when pacman.py is run
    from the command line:

    > python pacman.py

    See the usage string for more details.

    > python pacman.py --help
    """
   # args = readCommand(sys.argv[1:])  # Get game components based on input
    # runGames(**args)

    # import cProfile
    # cProfile.run("runGames( **args )")

    # should construct a new "Game" class with an initialized starting state
    # and graphics (if graphics have not been flagged off)

    display = CatanGraphics()

    state = State.generateState(NUM_PLAYERS)

    game = Game(display, state)

    game.run()
    pass
