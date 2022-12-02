import math
import random
import time
from Agents.Agent import Agent
from Agents.EvalFunctions import evalFuncVP
import Agents.KeyboardAgent


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

        # print("---\nDEBUG\n---")
        # print("minimax actions to choose:")
        # Agents.KeyboardAgent.printEnumeratedActions(actions)
        # print("---\nDEBUG\n---")

        if len(actions) == 1:
            print("Minimax Agent ", self.color.name,
                  "chose action ", actions[0].getActionAsString())
            return actions[0]

        bestActions = []

        value = -1 * math.inf

        for action in actions:
            print(action.getActionAsString())
            minimaxVal = 0
            className = type(action).__name__
            if className == "RollDice" or className == "DevelopmentCard" or className == "MoveRobber":
                allChances = action.getAllOutcomes(state)
                for prob, exact in allChances:
                    nextState = action.applyExact(state, exact)
                    minimaxVal += prob * \
                        self.minimax(nextState, self.depth,
                                     state.whoseTurn, -1)
            else:
                nextState = action.apply(state)
                minimaxVal = self.minimax(
                    nextState, self.depth, state.whoseTurn, -1)
            if minimaxVal > value:
                value = minimaxVal
                bestActions = [action]
            elif minimaxVal == value:
                bestActions.append(action)

        bestAction = bestActions[random.randint(0, len(bestActions) - 1)]

        print("Minimax Agent ", self.color.name,
              "chose action ", bestAction.getActionAsString())

        return bestAction

    def minimax(self, state, depth, maxPlayerIndex, prevPlayerActionIndex):
        agentIndex = state.whoseTurn

        actions = state.getValidActions()

        if state.isGameOver() or len(actions) == 0:
            return self.evaluationFunction(state)

        if agentIndex == maxPlayerIndex:  # Maximize for max player
            if depth == 0:
                return self.evaluationFunction(state)
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
                                         state.whoseTurn, -1)
                else:
                    nextState = action.apply(state)
                    minimaxVal = self.minimax(
                        nextState, depth - 1, state.whoseTurn, -1)
                value = max(value, minimaxVal)
            return value
        else:  # Minimize for enemy agents
            if depth == 0:
                return self.evaluationFunction(state)
            value = math.inf
            for action in actions:
                nextState = action.apply(state)
                value = min(value, self.minimax(
                    nextState, depth - 1, maxPlayerIndex, agentIndex))
            return value
