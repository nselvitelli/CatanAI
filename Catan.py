from Agents.MiniMaxAgent import MiniMaxAgent
from Agents.KeyboardAgent import KeyboardAgent
from Agents.RandomAgent import RandomAgent
from Agents.FirstActionAgent import FirstActionAgent
from Agents.AlphaBetaAgent import AlphaBetaAgent
from game import Game
from graphics.graphicsDisplay import CatanGraphics
from PlayerColor import PlayerColor
import State
import Agents.EvalFunctions



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

    agents = [
        # KeyboardAgent(PlayerColor.RED, cheats=True),
        # RandomAgent(PlayerColor.RED),
        # AlphaBetaAgent(PlayerColor.RED, depth=2, evaluationFunction=Agents.EvalFunctions.evalFuncCombineAll),
        MiniMaxAgent(PlayerColor.BLUE, depth=5, evaluationFunction=Agents.EvalFunctions.evalFuncCombineAll),
        MiniMaxAgent(PlayerColor.RED, depth = 5, evaluationFunction=Agents.EvalFunctions.createCustomEvalFuncCombineAll([1,1,100,10,1,10,10,10]))
        # AlphaBetaAgent(PlayerColor.BLUE, depth=5, evaluationFunction=Agents.EvalFunctions.evalFuncCombineAll)
        #RandomAgent(PlayerColor.BLUE),
        # RandomAgent(PlayerColor.ORANGE),
        # RandomAgent(PlayerColor.WHITE),
    ]

    state = State.generateState(agents)

    game = Game(display, state)

    game.run()
    pass
