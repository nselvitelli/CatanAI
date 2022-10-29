from Actions.Action import Action


class BuildCity(Action):

    def __init__(self, nodeID, playerColor) -> None:
        super().__init__(playerColor)
        self.nodeID = nodeID