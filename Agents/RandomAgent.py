from Agents.Agent import Agent
import random

class RandomAgent(Agent):

    def __init__(self, playerColor):
        self.color = playerColor

    def getAction(self, state):
        """
        The Agent will receive a GameState and must return an action
        """
        actions = state.getValidActions()
        if len(actions) == 1:
            action = actions[0]
        else:
            action = actions[random.randint(0, len(actions) - 1)]

        print("RandomAgent ", self.color.name, "chose action ", action.getActionAsString())

        return action
