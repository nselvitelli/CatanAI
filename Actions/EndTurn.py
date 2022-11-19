from Actions.Action import Action


class EndTurn(Action):

    # TODO: we need to come up with some way of tracking turn order...
    def __init__(self) -> None:
        super().__init__()