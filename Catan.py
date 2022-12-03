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


import multiprocessing
from multiprocessing import Process


def launchGames(numberGames, state):

    pool = multiprocessing.Pool()

    winnersMap = {}
    
    for result in pool.imap(playGame, list(map(lambda a: state, range(numberGames)))):
        if result in winnersMap.keys():
            winnersMap[result] += 1
        else:
            winnersMap[result] = 1
    
    print(winnersMap)

    # procs = []
    # for i in range(numberCPUs):
    #     proc = Process(target=playGame, args=(state,))
    #     proc.start()
    #     procs.append(proc)
    
    # for proc in procs:
    #     proc.join()
    # pass

def playGame(state):
    game = Game(None, state)
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

    display = CatanGraphics()

    agents = [
        # KeyboardAgent(PlayerColor.WHITE, cheats=True),
        RandomAgent(PlayerColor.RED),
        # AlphaBetaAgent(PlayerColor.ORANGE, depth=1, evaluationFunction=Agents.EvalFunctions.evalFuncCombineAll),
        MiniMaxAgent(PlayerColor.BLUE, depth=2, evaluationFunction=Agents.EvalFunctions.evalFuncCombineAll),
    ]

    numberGames = 3

    state = State.generateState(agents)

    launchGames(numberGames, state)

    # game = Game(display, state)
    # game.run()
    pass