from Actions.CheatAction import CheatAction
from Agents.Agent import Agent


class KeyboardAgent(Agent):

    def __init__(self, playerColor) -> None:
        super().__init__(playerColor)

    def getAction(self, state):
        """
        The Agent will receive a GameState and must return an action
        """
        actions = sorted(state.getValidActions(), key=lambda a: a.getActionAsString())

        actions.append(CheatAction()) # keyboard player can cheat for debugging

        print("Your valid actions are: ")
        self.printEnumeratedActions(actions)

        print("Type the index number of the action you want to use:")
        userData = input()
        index = None
        while not userData.isnumeric() or int(userData) >= len(actions):
            if not userData.isnumeric():
                print("Please input a positive integer:")
            else:
                print("Please choose an item within range:")
            userData = input()
        index = int(userData)
        print("Using action: ", actions[index].getActionAsString())

        return actions[index]

    def printEnumeratedActions(self, actions):
        for i in range(len(actions)):
            print("\t", i, ": ", actions[i].getActionAsString())
