from Actions.Action import Action


class DevelopmentCard(Action):

    def __init__(self) -> None:
        super().__init__()

    def apply(self, state):
        newState = state.getCopy()

        # not sure how many of each devcard exist...

        # note: i think victory point cards should be handled differently.
        # if its an action to appply our victory point that works, but i think the ai would just take that aciton immediately
        # idk tho could be fine
