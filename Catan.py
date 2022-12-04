from Agents.MaxiMaxAgent import MaxiMaxAgent
from Agents.KeyboardAgent import KeyboardAgent
from Agents.MiniMaxAgent import MiniMaxAgent
from Agents.RandomAgent import RandomAgent
from Agents.FirstActionAgent import FirstActionAgent
from Agents.AlphaBetaAgent import AlphaBetaAgent
from Node import NodePiece
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

    def errorCallback(self, error):
        print(bcolors.FAIL + "ERROR:", error, bcolors.ENDC)

    def gameProcessCallback(self, result):
        self.gamesComplete += 1
        print(bcolors.OKGREEN, "### Completed game", self.gamesComplete, "out of", self.numberGames, "###", bcolors.ENDC)

        players = result.playerDataList

        for player in players:
            playerCol = player.color
            vp = player.victoryPoints

            numSettlements = 0
            numCities = 0
            playerPieces = list(map(lambda a: result.board.nodes[a].piece[0], player.settlements))
            for piece in playerPieces:
                if piece == NodePiece.CITY:
                    numCities += 1
                elif piece == NodePiece.SETTLEMENT:
                    numSettlements += 1

            if playerCol in self.statsMap.keys():
                increaseAverage = lambda key, val: ((self.statsMap[playerCol][key] * (self.gamesComplete - 1)) + val) / self.gamesComplete
                self.statsMap[playerCol]['VP'] = increaseAverage('VP', vp)
                self.statsMap[playerCol]['SETTLEMENTS'] = increaseAverage('SETTLEMENTS', numSettlements)
                self.statsMap[playerCol]['CITIES'] = increaseAverage('CITIES', numCities)
            else:
                self.statsMap[playerCol] = {}
                self.statsMap[playerCol]['VP'] = vp
                self.statsMap[playerCol]['SETTLEMENTS'] = numSettlements
                self.statsMap[playerCol]['CITIES'] = numCities
                self.statsMap[playerCol]['WINS'] = 0

        winnerCol = result.getWinner().color
        self.statsMap[winnerCol]['WINS'] += 1

    def launchGames(self):

        numPools = min(self.numberGames, multiprocessing.cpu_count())
        pool = multiprocessing.Pool(1)

        self.winnersMap = {}
        self.gamesComplete = 0

        startTime = time.time()

        for i in range(self.numberGames):
            print(bcolors.OKGREEN, "### Launching Game" + bcolors.WARNING, str(i + 1), bcolors.OKGREEN + "###", bcolors.ENDC)
            pool.apply_async(playGame, args=(self.state,), callback=self.gameProcessCallback, error_callback=self.errorCallback)   
         
        pool.close()    
        pool.join()

        for color, stats in self.statsMap.items():
            wins = stats['WINS'] 
            percent = "{:.2f}".format(100 * (wins / self.numberGames))
            vp = "{:.2f}".format(stats['VP'])
            settlements = "{:.2f}".format(stats['SETTLEMENTS'])
            cities = "{:.2f}".format(stats['CITIES'])
            print(bcolors.OKGREEN, color.name, bcolors.OKCYAN + "agent won", wins, "game(s). Win Rate:" + bcolors.WARNING, percent + '%', bcolors.ENDC)
            print(bcolors.OKCYAN, "- average VP:", vp, bcolors.ENDC)
            print(bcolors.OKCYAN, "- average Settlements:", settlements, bcolors.ENDC)
            print(bcolors.OKCYAN, "- average Cities:", cities, bcolors.ENDC)

        endTime = time.time()
        print(bcolors.OKCYAN, self.gamesComplete, "games completed in" + bcolors.OKGREEN, '{:0.2f}'.format(endTime - startTime), bcolors.OKCYAN + "seconds", bcolors.ENDC)


if __name__ == '__main__':
    # should construct a new "Game" class with an initialized starting state
    # and graphics (if graphics have not been flagged off)

    agents = [
        # KeyboardAgent(PlayerColor.RED, cheats=True),
        AlphaBetaAgent(PlayerColor.RED, depth=1, evaluationFunction=Agents.EvalFunctions.evalFuncCombineAll, loud=False),
        AlphaBetaAgent(PlayerColor.WHITE, depth=3, evaluationFunction=Agents.EvalFunctions.evalFuncCombineAll, loud=False),
        # MaxiMaxAgent(PlayerColor.BLUE, depth=3, evaluationFunction=Agents.EvalFunctions.evalFuncCombineAll, loud=False),
        # MiniMaxAgent(PlayerColor.RED, depth=4, evaluationFunction=Agents.EvalFunctions.createCustomEvalFuncCombineAll([1,1,10,10,20,10,10,10]))
        # AlphaBetaAgent(PlayerColor.BLUE, depth=5, evaluationFunction=Agents.EvalFunctions.evalFuncCombineAll)
        #RandomAgent(PlayerColor.BLUE),
        # RandomAgent(PlayerColor.ORANGE, loud=False),
        # RandomAgent(PlayerColor.WHITE, loud=False),
    ]

    state = State.generateState(agents)
    
    RunMultipleGames(numberGames=100, state=state).launchGames()

    # playGame(state, CatanGraphics())

    pass
