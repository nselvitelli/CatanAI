from Actions.Action import Action


class BuildRoad(Action):

    def __init__(self, edgeID, playerColor) -> None:
        super().__init__(playerColor)
        self.edgeID = edgeID
