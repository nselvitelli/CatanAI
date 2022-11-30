from Agents.Agent import Agent
from Agents.EvalFunctions import evalFuncVP

class MiniMaxAgent(Agent):

    def __init__(self, color, depth=3, evalFunc=evalFuncVP) -> None:
        super().__init__(color)
        self.depth = depth
        self.evalFunc = evalFunc

    def getAction(self, state):
        """
        Do Minimax to self.depth with self.evalFunc
        """