from Actions.Action import Action


class BuildCity(Action):

    def __init__(self, nodeID) -> None:
        super().__init__()
        self.nodeID = nodeID