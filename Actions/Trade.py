from Actions.Action import Action


class BuildCity(Action):

    def __init__(self, resource) -> None:
        super().__init__()
        self.resource = resource