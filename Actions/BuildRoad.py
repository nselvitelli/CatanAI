from Actions.Action import Action


class BuildRoad(Action):

    def __init__(self, edgeID) -> None:
        super().__init__()
        self.edgeID = edgeID