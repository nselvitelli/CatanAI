from Agents.Agent import Agent
import random

class FirstActionAgent(Agent):

    def __init__(self, playerColor):
        self.color = playerColor

    def getAction(self, state):
        """
        The Agent will receive a GameState and must return an action
        """
        actions = state.getValidActions()
        action = actions[0]

        print("FirstActionAgent ", self.color.name, "chose action ", action.getActionAsString())

        return action
