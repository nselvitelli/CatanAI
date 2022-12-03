import math
import random
import time
from Agents.Agent import Agent
from Agents.EvalFunctions import evalFuncVP
import Agents.KeyboardAgent


class MaxiMaxAgent(Agent):

    def __init__(self, color, depth=3, evaluationFunction=evalFuncVP) -> None:
        super().__init__(color)
        self.depth = depth
        self.evaluationFunction = evaluationFunction

    def getAction(self, state):
        """
        Do Maximax to self.depth with self.evalFunc
        """

        actions = state.getValidActions()

        # print("---\nDEBUG\n---")
        # print("maximax actions to choose:")
        # Agents.KeyboardAgent.printEnumeratedActions(actions)
        # print("---\nDEBUG\n---")

        if len(actions) == 1:
            print("Maximax Agent ", self.color.name,
                  "chose action ", actions[0].getActionAsString())
            return actions[0]

        bestActions = []
        agentIndex = state.whoseTurn
        values = []
        #initializes values to all be minvalue, these store currently found max
        for player in state.playerDataList :
            values.append(-1 * math.inf)

        for action in actions:
            #initializes all maxValues to 0, used for expectimax
            maxValues = []
            for player in state.playerDataList :
                maxValues.append(0)

            className = type(action).__name__
            #expectimax
            if className == "RollDice" or className == "DevelopmentCard" or className == "MoveRobber":
                allChances = action.getAllOutcomes(state)
                for prob, exact in allChances:
                    nextState = action.applyExact(state, exact)
                    actionMaxValues = self.maximax(nextState, self.depth)
                    i = 0
                    for actionMaxValue in actionMaxValues :
                        maxValues[i] += prob * actionMaxValue
                        i += 1
            else:
                nextState = action.apply(state)
                maxValues = self.maximax(
                    nextState, self.depth)
            if maxValues[agentIndex] > values[agentIndex] :
                values = maxValues
                bestActions = [action]
            elif maxValues[agentIndex] == values[agentIndex]:
                bestActions.append(action)

        bestAction = bestActions[random.randint(0, len(bestActions) - 1)]

        print("Maximax Agent ", self.color.name,
              "chose action ", bestAction.getActionAsString())

        return bestAction

    def maximax(self, state, depth):
        agentIndex = state.whoseTurn

        actions = state.getValidActions()

        if state.isGameOver() or len(actions) == 0:
            return self.evaluate(state)
        if depth == 0:
            return self.evaluate(state)

        values = []
        for player in state.playerDataList :
            values.append(-1 * math.inf)

        for action in actions:
            maxValues = []
            for player in state.playerDataList :
                maxValues.append(0)

            className = type(action).__name__
            if className == "RollDice" or className == "DevelopmentCard" or className == "MoveRobber":
                allChances = action.getAllOutcomes(state)
                for prob, exact in allChances:
                    nextState = action.applyExact(state, exact)
                    actionMaxValues = self.maximax(nextState, depth - 1)
                    i = 0
                    for actionMaxValue in actionMaxValues :
                        maxValues[i] += prob * actionMaxValue
                        i += 1
            else:
                nextState = action.apply(state)
                maxValues = self.maximax(
                    nextState, depth - 1)
            if maxValues[agentIndex] > values[agentIndex] :
                values = maxValues
        return values

    def evaluate(self, state) :
        values = []
        for index, player in enumerate(state.playerDataList):
            values.append(self.evaluationFunction(state, index))
        return values

# idea:
    # eval functions return an array of size number of players
    # we know agent index from whoseturn
    # each agent maximized their own position in array
