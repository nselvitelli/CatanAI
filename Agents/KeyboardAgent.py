from Actions.CheatAction import CheatAction
from Agents.Agent import Agent


class KeyboardAgent(Agent):

    def __init__(self, playerColor, cheats=False) -> None:
        super().__init__(playerColor, True)
        self.cheats = cheats

    def getAction(self, state):
        """
        The Agent will receive a GameState and must return an action
        """
        actions = sorted(state.getValidActions(), key=lambda a: a.getActionAsString())

        if self.cheats:
            actions.append(CheatAction()) # keyboard player can cheat for debugging

        print("Your valid actions are: ")
        printEnumeratedActions(actions)

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

def printEnumeratedActions(actions):
    for i in range(len(actions)):
        print("\t", i, ": ", actions[i].getActionAsString())
