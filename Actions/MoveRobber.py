from Actions.Action import Action
from Board import Board


class MoveRobber(Action):

    def __init__(self, tileID, stealPlayer) -> None:
        super().__init__()
        self.tileID = tileID
        self.stealPlayer = stealPlayer

    def apply(self, state):
        board = Board(state.board.tiles, state.board.nodes,
                      state.board.edges, tileID)

        actionTakerData =
        stealData = state.playerDataDict[]

        # construct a new board...
