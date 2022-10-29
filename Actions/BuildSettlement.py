from Actions.Action import Action


class BuildSettlement(Action):

    def __init__(self, nodeID, playerColor) -> None:
        super().__init__()
        self.nodeID = nodeID
        self.playerColor = playerColor