import math
import random
from Agents.Agent import Agent
from Agents.EvalFunctions import evalFuncVP


class MiniMaxAgent(Agent):

    def __init__(self, color, depth=3, evaluationFunction=evalFuncVP, loud=True) -> None:
        super().__init__(color, loud)
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
            if self.loud :
                print("Minimax Agent ", self.color.name,
                    "chose action ", actions[0].getActionAsString())
            return actions[0]

        bestActions = []

        value = -1 * math.inf

        for action in actions:
            minimaxVal = 0
            className = type(action).__name__
            if className == "RollDice" or className == "DevelopmentCard" or className == "MoveRobber":
                allChances = action.getAllOutcomes(state)
                for prob, exact in allChances:
                    nextState = action.applyExact(state, exact)
                    minimaxVal += prob * \
                        self.minimax(nextState, self.depth,
                                     state.whoseTurn)
            else:
                nextState = action.apply(state)
                minimaxVal = self.minimax(
                    nextState, self.depth, state.whoseTurn)
            if minimaxVal > value:
                value = minimaxVal
                bestActions = [action]
            elif minimaxVal == value:
                bestActions.append(action)

        bestAction = bestActions[random.randint(0, len(bestActions) - 1)]

        if self.loud:
            print("Minimax Agent ", self.color.name,
                "chose action ", bestAction.getActionAsString())

        return bestAction

    def minimax(self, state, depth, maxPlayerIndex):
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
                                         maxPlayerIndex)
                else:
                    nextState = action.apply(state)
                    minimaxVal = self.minimax(
                        nextState, depth - 1, maxPlayerIndex)
                value = max(value, minimaxVal)
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
                                         maxPlayerIndex)
                else:
                    nextState = action.apply(state)
                    minimaxVal = self.minimax(
                        nextState, depth - 1, maxPlayerIndex)
                value = min(value, minimaxVal)
            return value