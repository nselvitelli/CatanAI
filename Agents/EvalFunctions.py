from Node import NodePiece
from Resource import Resource


def evalFuncZero(state) -> int:
    """
    Control eval func used to compare against any other eval funcs we make.
    """
    return 0

def createCustomEvalFuncCombineAll(weights):
    return lambda state, maximizingPlayer: evalFuncCombineAll(state, maximizingPlayer, weights)

def evalFuncCombineAll(state, maximizingPlayer, weights = None) -> int:
    weightsAndFunctions = [
        (evalFuncRealEstate, 1),
        (evalFuncResourceDiversity, 20),
        (evalFuncVP, 1),
        (evalFuncRobberOnLand, 10),
        (evalFuncRichResources, 10),
        (evalFuncLessThan8Resources, 10),
        (evalFuncLargestArmy, 10),
        (evalFuncLongestRoad, 10)
    ] if weights == None else [
        (evalFuncRealEstate, weights[0]),
        (evalFuncResourceDiversity, weights[1]),
        (evalFuncVP, weights[2]),
        (evalFuncRobberOnLand, weights[3]),
        (evalFuncRichResources, weights[4]),
        (evalFuncLessThan8Resources, weights[5]),
        (evalFuncLargestArmy, weights[6]),
        (evalFuncLongestRoad, weights[7])
    ]

    score = 0
    for tuple in weightsAndFunctions:
        score += tuple[1] * tuple[0](state, maximizingPlayer)
    return score

def evalFuncVP(state, maximizingPlayer) -> int:
    """
    Determines score of state for current player in State 'state'
    by subtracting the number of victory points the 'whoseTurn player' has by the average number
    of victory points every player has.
    """
    averageVP = 0
    for player in state.playerDataList:
        averageVP += player.victoryPoints
    averageVP /= len(state.playerDataList)

    return state.playerDataList[maximizingPlayer].victoryPoints - averageVP

def evalFuncRealEstate(state, maximizingPlayer) -> int:
    """
    Determines score for which player by getting total num of settlements and cities and subtracting that by the average of every other player
    """

    currentPlayer = state.playerDataList[maximizingPlayer]
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

def evalFuncResourceDiversity(state, maximizingPlayer) -> int:
    """
    Scored on how many resources the current player has access to
    """
    resources = set([Resource.WHEAT, Resource.BRICK, Resource.LOG, Resource.ORE, Resource.SHEEP])

    player = state.playerDataList[maximizingPlayer]

    for tile in state.board.tiles.values():
        for nodeID in tile.nodes:
            node = state.board.nodes[nodeID]
            if node.piece[0] != NodePiece.EMPTY and node.piece[1] == player.color:
                resources -= set([tile.resource])

    return 5 - len(resources)

def evalFuncRobberOnLand(state, maximizingPlayer) -> int:
    """
        1 if the current player does not have a robber on one of their nodes
        0 if they do have the robber blocking them
    """
    player = state.playerDataList[maximizingPlayer]

    robber_tile = state.board.robber_tile

    robberNodes = set(state.board.tiles[robber_tile].nodes)
    playerNodes = set(player.settlements)

    if len(playerNodes - robberNodes) < len(playerNodes):
        return 0
    return 1

def evalFuncRichResources(state, maximizingPlayer) -> int:
    """
    Calculates a score for each tile the player is on based on how rich the resources are at that tile
    Sums score for each tile to get final score
    
    for each tile:
    - get num resources the current player would get if the number was rolled
    - score the roll number from [1, 6] (6 is most common, so - 6 = roll(7), 5 = roll(6, 8), etc.)
    - get product of two values
    - add product to the total score
    """
    player = state.playerDataList[maximizingPlayer]

    # 2 - 12
    # 7 is most common
    totalPlayerRichTileScore = 0

    for tile in state.board.tiles.values():

        numResourcesGottenFromTile = 0
        for nodeID in tile.nodes:
            node = state.board.nodes[nodeID]
            if node.piece[1] == player.color:
                numResourcesGottenFromTile += 1 if node.piece[0] == NodePiece.SETTLEMENT else 2
        
        resourceFreq = 6 - abs(7 - tile.number) # scores number from [1, 6]  (6 being very common, 1 being very uncommon)
        tileScore = numResourcesGottenFromTile * resourceFreq
        totalPlayerRichTileScore += tileScore
    return totalPlayerRichTileScore

def evalFuncLessThan8Resources(state, maximizingPlayer) -> int:
    """
    1 if less than 8 resources in hand
    0 if more than 7
    """
    player = state.playerDataList[maximizingPlayer]

    totalAmt = 0
    for resourceAmt in player.resourcesAvailable.values():
        totalAmt += resourceAmt

    if totalAmt > 7:
        return 0
    return 1

def evalFuncLargestArmy(state, maximizingPlayer) -> int:
    """
    1 if player has largest army
    0 if player doesn't
    """
    return 1 if maximizingPlayer == state.largestArmy else 0

def evalFuncLongestRoad(state, maximizingPlayer) -> int:
    """
    1 if player has longest road
    0 if player doesn;t
    """
    return 1 if maximizingPlayer == state.longestRoad else 0