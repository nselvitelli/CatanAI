from Agents.Agent import Agent
from Agents.EvalFunctions import evalFuncVP
import math


class AlphaBetaAgent(Agent):

    def __init__(self, color, depth=3, evaluationFunction=evalFuncVP) -> None:
        super().__init__(color)
        self.depth = depth
        self.evaluationFunction = evaluationFunction

    def getAction(self, state):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """

        actions = state.getValidActions()
        bestAction = actions[0]
        value = -1 * math.inf
        alpha = -1 * math.inf
        beta = math.inf
        for action in actions:
            nextState = action.apply(state)
            minimaxVal = self.minimax(
                nextState, self.depth, state.whoseTurn, alpha, beta)
            if minimaxVal > value:
                bestAction = action
                value = minimaxVal
            alpha = max(alpha, minimaxVal)

        print("Minimax Agent ", self.color.name,
              "chose action ", bestAction.getActionAsString())

        return bestAction

    def minimax(self, gameState, depth, maxPlayerIndex, alpha, beta):
        agentIndex = gameState.whoseTurn
        actions = gameState.getValidActions()

        if gameState.isGameOver() or len(actions) == 0:
            return self.evaluationFunction(gameState)

        if agentIndex == maxPlayerIndex:  # Maximize for max player
            if depth == 0:
                return self.evaluationFunction(gameState)
            value = -1 * math.inf
            for action in actions:
                nextState = action.apply(gameState)
                value = max(value, self.minimax(
                    nextState, depth, maxPlayerIndex, alpha, beta))
                if value > beta:
                    return value
                alpha = max(alpha, value)
            return value
        else:  # Minimize for ghosts
            value = math.inf
            for action in actions:
                nextState = action.apply(gameState)
                if nextState.whoseTurn == maxPlayerIndex:
                    depth = depth - 1
                value = min(value, self.minimax(
                    nextState, depth, maxPlayerIndex, alpha, beta))
                if value < alpha:
                    return value
                beta = min(beta, value)
            return value
