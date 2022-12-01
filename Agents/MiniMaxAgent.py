import math
import random
from Agents.Agent import Agent
from Agents.EvalFunctions import evalFuncVP

class MiniMaxAgent(Agent):

    def __init__(self, color, depth=3, evaluationFunction=evalFuncVP) -> None:
        super().__init__(color)
        self.depth = depth
        self.evaluationFunction = evaluationFunction

    def getAction(self, state):
        """
        Do Minimax to self.depth with self.evalFunc
        """

        actions = state.getValidActions()

        if len(actions) == 1:
            return actions[0]

        bestActions = []

        value = -1 * math.inf

        for action in actions:
            nextState = action.apply(state)
            minimaxVal = self.minimax(nextState, self.depth, state.whoseTurn, -1)
            if minimaxVal > value:
                value = minimaxVal
                bestActions = [action]
            elif minimaxVal == value:
                bestActions.append(action)
            
        bestAction = bestActions[random.randint(0, len(bestActions) - 1)]
        
        print("Minimax Agent ", self.color.name, "chose action ", bestAction.getActionAsString())

        return bestAction


    def minimax(self, gameState, depth, maxPlayerIndex, prevPlayerActionIndex):
        agentIndex = gameState.whoseTurn

        actions = gameState.getValidActions()

        if gameState.isGameOver() or len(actions) == 0:
            return self.evaluationFunction(gameState)

        if agentIndex == maxPlayerIndex: # Maximize for max player
            if agentIndex != prevPlayerActionIndex:
                depth = depth - 1
            if depth == 0:
                return self.evaluationFunction(gameState)
            value = -1 * math.inf
            for action in actions:
                nextState = action.apply(gameState)
                value = max(value, self.minimax(nextState, depth, maxPlayerIndex, agentIndex))
            return value
        else: # Minimize for enemy agents
            value = math.inf
            for action in actions:
                nextState = action.apply(gameState)
                value = min(value, self.minimax(nextState, depth, maxPlayerIndex, agentIndex))
            return value