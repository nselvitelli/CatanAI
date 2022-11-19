from Agent import Agent


class KeyboardAgent(Agent):

    def __init__(self, playerColor) -> None:
        super().__init__(playerColor)

    def getAction(self, state):
        """
        The Agent will receive a GameState and must return an action
        """
        actions = state.getValidActions()

        print("Your valid actions are: ")
        self.printEnumeratedActions(actions)

        print("Type the index number of the action you want to use:")
        index = int(input())

        print("Using action: ", actions[index].getActionAsString())

        return actions[index]

    def printEnumeratedActions(self, actions):
        for i in range(len(actions)):
            print("\t", i, ": ", actions[i].getActionAsString(), "\n")

