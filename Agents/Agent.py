class Agent:

    def __init__(self, playerColor, loud):
        self.color = playerColor
        self.loud = loud


    def getAction(self, state):
        """
        The Agent will receive a GameState and must return an action
        """
