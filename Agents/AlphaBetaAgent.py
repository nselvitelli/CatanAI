from Agents.Agent import Agent
from Agents.EvalFunctions import evalFuncVP
import math
import random


class AlphaBetaAgent(Agent):

    def __init__(self, color, depth=3, evaluationFunction=evalFuncVP, loud=True) -> None:
        super().__init__(color, loud)
        self.depth = depth
        self.evaluationFunction = evaluationFunction

    def getAction(self, state):
        """
        Do Minimax to self.depth with self.evalFunc
        """

        actions = state.getValidActions()

        if len(actions) == 1:
            if self.loud:
                print("AlphaBeta Agent ", self.color.name,
                "chose action ", actions[0].getActionAsString())
            return actions[0]

        bestActions = []

        value = -1 * math.inf
        alpha = -1 * math.inf
        beta = math.inf
        for action in actions:
            minimaxVal = 0
            className = type(action).__name__
            if className == "RollDice" or className == "DevelopmentCard" or className == "MoveRobber":
                allChances = action.getAllOutcomes(state)
                for prob, exact in allChances:
                    nextState = action.applyExact(state, exact)
                    minimaxVal += prob * \
                        self.minimax(nextState, self.depth,
                                     state.whoseTurn, -1, alpha, beta)
            else:
                nextState = action.apply(state)
                minimaxVal = self.minimax(
                    nextState, self.depth, state.whoseTurn, -1, alpha, beta)
            if minimaxVal > value:
                value = minimaxVal
                bestActions = [action]
            elif minimaxVal == value:
                bestActions.append(action)
            alpha = max(alpha, minimaxVal)

        bestAction = bestActions[random.randint(0, len(bestActions) - 1)]

        if self.loud:
            print("AlphaBeta Agent ", self.color.name,
                "chose action ", bestAction.getActionAsString())

        return bestAction

    def minimax(self, state, depth, maxPlayerIndex, prevPlayerActionIndex, alpha, beta):
        agentIndex = state.whoseTurn

        actions = state.getValidActions()

        if state.isGameOver() or len(actions) == 0:
            return self.evaluationFunction(state, maxPlayerIndex)

        if agentIndex == maxPlayerIndex:  # Maximize for max player
            if depth == 0:
                return self.evaluationFunction(state, maxPlayerIndex)

            value = -1 * math.inf
            for action in actions:
                minimaxVal = 0
                className = type(action).__name__
                if className == "RollDice" or className == "DevelopmentCard" or className == "MoveRobber":
                    allChances = action.getAllOutcomes(state)
                    for prob, exact in allChances:
                        nextState = action.applyExact(state, exact)
                        minimaxVal += prob * \
                            self.minimax(nextState, depth - 1,
                                        maxPlayerIndex, agentIndex, alpha, beta)
                else:
                    nextState = action.apply(state)
                    minimaxVal = self.minimax(
                        nextState, depth - 1, maxPlayerIndex, agentIndex, alpha, beta)
                value = max(value, minimaxVal)
                if value > beta:
                    return value
                alpha = max(alpha, value)
            return value
        else:  # Minimize for enemy agents
            if depth == 0:
                return self.evaluationFunction(state, maxPlayerIndex)

            value = math.inf
            for action in actions:
                minimaxVal = 0
                className = type(action).__name__
                if className == "RollDice" or className == "DevelopmentCard" or className == "MoveRobber":
                    allChances = action.getAllOutcomes(state)
                    for prob, exact in allChances:
                        nextState = action.applyExact(state, exact)
                        minimaxVal += prob * \
                            self.minimax(nextState, depth - 1,
                                        maxPlayerIndex, agentIndex, alpha, beta)
                else:
                    nextState = action.apply(state)
                    minimaxVal = self.minimax(
                        nextState, depth - 1, maxPlayerIndex, agentIndex, alpha, beta)
                value = - max(value, minimaxVal)
                if value < alpha:
                    return value
                beta = min(beta, value)
            return value
