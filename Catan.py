from Agents.MaxiMaxAgent import MaxiMaxAgent
from Agents.KeyboardAgent import KeyboardAgent
from Agents.RandomAgent import RandomAgent
from Agents.FirstActionAgent import FirstActionAgent
from Agents.AlphaBetaAgent import AlphaBetaAgent
from game import Game
from graphics.graphicsDisplay import CatanGraphics
from PlayerColor import PlayerColor
import State
import Agents.EvalFunctions

import multiprocessing

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def launchGames(numberGames, state):

    pool = multiprocessing.Pool()

    winnersMap = {}
    gamesComplete = 0

    for result in pool.imap(playGame, list(map(lambda a: state, range(numberGames)))):
        gamesComplete += 1
        print(bcolors.OKGREEN, "### Completed game", gamesComplete, "out of", numberGames, "###", bcolors.ENDC)
        if result in winnersMap.keys():
            winnersMap[result] += 1
        else:
            winnersMap[result] = 1
    
    for color, wins in winnersMap.items():
        percent = 100 * (wins/numberGames)
        print(bcolors.OKCYAN, color.name, "agent won", wins, "games. Win Rate:" + bcolors.WARNING, str(percent) + "%", bcolors.ENDC)

    # procs = []
    # for i in range(numberCPUs):
    #     proc = Process(target=playGame, args=(state,))
    #     proc.start()
    #     procs.append(proc)
    
    # for proc in procs:
    #     proc.join()
    # pass

def playGame(state):
    game = Game(CatanGraphics(), state)
    return game.run()


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

    

    agents = [
        # KeyboardAgent(PlayerColor.RED, cheats=True),
        RandomAgent(PlayerColor.RED),
        # AlphaBetaAgent(PlayerColor.RED, depth=2, evaluationFunction=Agents.EvalFunctions.evalFuncCombineAll),
        MaxiMaxAgent(PlayerColor.BLUE, depth=2, evaluationFunction=Agents.EvalFunctions.evalFuncCombineAll),
        # MiniMaxAgent(PlayerColor.RED, depth=4, evaluationFunction=Agents.EvalFunctions.createCustomEvalFuncCombineAll([1,1,10,10,20,10,10,10]))
        # AlphaBetaAgent(PlayerColor.BLUE, depth=5, evaluationFunction=Agents.EvalFunctions.evalFuncCombineAll)
        #RandomAgent(PlayerColor.BLUE),
        RandomAgent(PlayerColor.ORANGE),
        # RandomAgent(PlayerColor.WHITE),
    ]

    numberGames = 1

    state = State.generateState(agents)
    

    launchGames(numberGames, state)

    # display = CatanGraphics()
    # game = Game(display, state)
    # game.run()
    pass