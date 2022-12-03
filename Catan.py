from Agents.MaxiMaxAgent import MaxiMaxAgent
from Agents.KeyboardAgent import KeyboardAgent
from Agents.MiniMaxAgent import MiniMaxAgent
from Agents.RandomAgent import RandomAgent
from Agents.FirstActionAgent import FirstActionAgent
from Agents.AlphaBetaAgent import AlphaBetaAgent
from game import Game
from graphics.graphicsDisplay import CatanGraphics
from PlayerColor import PlayerColor
import State
import Agents.EvalFunctions


import multiprocessing
import time

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



def playGame(state, display=None):
    game = Game(display, state)
    return game.run()

class RunMultipleGames:

    def __init__(self, numberGames, state) -> None:
        self.gamesComplete = 0
        self.numberGames = numberGames
        self.state = state
        self.statsMap = {}

    def gameProcessCallback(self, result):
        self.gamesComplete += 1
        print(bcolors.OKGREEN, "### Completed game", self.gamesComplete, "out of", self.numberGames, "###", bcolors.ENDC)

        players = result.playerDataList

        for player in players:
            playerCol = player.color
            if playerCol in self.statsMap.keys():
                self.statsMap[playerCol]['VP'] = ((self.statsMap[playerCol]['VP'] * (self.gamesComplete - 1)) + player.victoryPoints) / self.gamesComplete
            else:
                self.statsMap[playerCol] = {}
                self.statsMap[playerCol]['VP'] = player.victoryPoints

        winnerCol = result.getWinner().color
        if 'WINS' in self.statsMap[winnerCol].keys():
            self.statsMap[winnerCol]['WINS'] += 1
        else:
            self.statsMap[winnerCol]['WINS'] = 1
        return
            


    def launchGames(self):

        pool = multiprocessing.Pool()

        self.winnersMap = {}
        self.gamesComplete = 0

        startTime = time.time()

        for i in range(self.numberGames):
            print(bcolors.OKGREEN, "### Launching Game" + bcolors.WARNING, str(i + 1), bcolors.OKGREEN + "###", bcolors.ENDC)
            pool.apply_async(playGame, args=(self.state,), callback=self.gameProcessCallback)   
         
        pool.close()    
        pool.join()
        print("done")

        for color, stats in self.statsMap.items():
            wins = stats['WINS']
            percent = 100 * (wins / self.numberGames)
            print(bcolors.OKCYAN, color.name, "agent won", wins, "games. Win Rate:" + bcolors.WARNING, str(percent) + "%", bcolors.ENDC)
            print(bcolors.OKCYAN, "- average VP:", stats['VP'], bcolors.ENDC)

        endTime = time.time()
        print(bcolors.OKCYAN, self.numberGames, "games completed in" + bcolors.OKGREEN, endTime - startTime, bcolors.OKCYAN + "seconds", bcolors.ENDC)


if __name__ == '__main__':
    # should construct a new "Game" class with an initialized starting state
    # and graphics (if graphics have not been flagged off)

    agents = [
        # KeyboardAgent(PlayerColor.RED, cheats=True),
        MiniMaxAgent(PlayerColor.RED, depth=3, evaluationFunction=Agents.EvalFunctions.evalFuncCombineAll, loud=False),
        AlphaBetaAgent(PlayerColor.WHITE, depth=3, evaluationFunction=Agents.EvalFunctions.evalFuncCombineAll, loud=False),
        MaxiMaxAgent(PlayerColor.BLUE, depth=3, evaluationFunction=Agents.EvalFunctions.evalFuncCombineAll, loud=False),
        # MiniMaxAgent(PlayerColor.RED, depth=4, evaluationFunction=Agents.EvalFunctions.createCustomEvalFuncCombineAll([1,1,10,10,20,10,10,10]))
        # AlphaBetaAgent(PlayerColor.BLUE, depth=5, evaluationFunction=Agents.EvalFunctions.evalFuncCombineAll)
        #RandomAgent(PlayerColor.BLUE),
        RandomAgent(PlayerColor.ORANGE, loud=False),
        # RandomAgent(PlayerColor.WHITE, loud=False),
    ]

    state = State.generateState(agents)
    
    RunMultipleGames(numberGames=2, state=state).launchGames()

    # playGame(state, CatanGraphics())

    pass
