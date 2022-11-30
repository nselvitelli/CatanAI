from Node import NodePiece
from Resource import Resource


def evalFuncZero(state) -> int:
    """
    Control eval func used to compare against any other eval funcs we make.
    """
    return 0

def evalFuncVP(state) -> int:
    """
    Determines score of state for current player in State 'state'
    by subtracting the number of victory points the 'whoseTurn player' has by the average number
    of victory points every player has.
    """
    averageVP = 0
    for player in state.playerDataList:
        averageVP += player.victoryPoints
    averageVP /= len(state.playerDataList)

    return state.playerDataList[state.whoseTurn].victoryPoints - averageVP

def evalFuncRealEstate(state) -> int:
    """
    Determines score for which player by getting total num of settlements and cities and subtracting that by the average of every other player
    """

    currentPlayer = state.playerDataList[state.whoseTurn]
    playerScore = scorePlayerSettlements(state, currentPlayer)

    avgScore = 0
    for player in state.playerDataList:
        avgScore += scorePlayerSettlements(state, player)
    avgScore /= len(state.playerDataList)

    return (int)(playerScore - avgScore)

def scorePlayerSettlements(state, player) -> int:
    """
    Scores a single player based on the number of settlements and cities they have.
    Cities count as two settlements
    """
    playerScore = 0
    for nodeID in player.settlements:
        if state.board.nodes[nodeID].piece[0] == NodePiece.CITY:
            playerScore += 2
        elif state.board.nodes[nodeID].piece[0] == NodePiece.SETTLEMENT:
            playerScore += 1
    return playerScore


def evalFuncResourceDiversity(state) -> int:
    """
    Scored on how many resources the current player has access to
    """
    resources = set([Resource.WHEAT, Resource.BRICK, Resource.LOG, Resource.ORE, Resource.SHEEP])

    player = state.playerDataList[state.whoseTurn]

    for tile in state.board.tiles:
        for nodeID in tile.nodes:
            node = state.board.nodes[nodeID]
            if node[0] != NodePiece.EMPTY and node[1] == player.color:
                resources -= set([tile.resource])

    return 5 - len(resources)