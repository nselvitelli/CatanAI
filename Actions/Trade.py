from Actions.Action import Action


class Trade(Action):

    def __init__(self, resource, quantity) -> None:
        super().__init__()
        self.resource = resource
        self.quantity = quantity