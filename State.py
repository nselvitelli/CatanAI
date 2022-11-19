from Actions.BuildCity import BuildCity
from Actions.BuildRoad import BuildRoad
from Actions.BuildSettlement import BuildSettlement
from Actions.DevelopmentCard import DevelopmentCard
from Actions.EndTurn import EndTurn
from Actions.NextPlayer import NextPlayer
from Actions.Trade import Trade
from Actions.Action import EAction
from Actions.MoveRobber import MoveRobber
from Actions.RollDice import RollDice
from Actions.Discard import Discard
from Board import Board
from DevCard import DevCardName
from Node import NodePiece, Port
from PlayerColor import PlayerColor
from PlayerData import PlayerData

from Resource import Resource

class State:

    def __init__(self, board, playerDataList, devCards, longestRoad, largestArmy, whoseTurn, necessaryActions) -> None:
        self.board = board
        self.playerDataList = playerDataList
        self.devCards = devCards
        self.whoseTurn = whoseTurn  # this is an index
        self.longestRoad = longestRoad
        self.largestArmy = largestArmy
        self.necessaryActions = necessaryActions

    def getCopy(self):
        newBoard = self.board.getCopy()
        newPlayerDataList = []
        for ind in enumerate(self.playerDataList):
            newPlayerDataList.append(self.playerDataList[ind].getCopy())

        newDevCards = []
        for devCard in self.devCards:
            newDevCards.append(devCard)

        newNecessaryActions = []
        for action in self.necessaryActions:
            newNecessaryActions.append(action)

        return State(newBoard, newPlayerDataList, newDevCards, self.longestRoad, self.largestArmy, self.whoseTurn, newNecessaryActions)

    def getValidActions(self):

        if len(self.necessaryActions) > 0:
            return self.getNecessaryActions()

        currentPlayer = self.playerDataList[self.whoseTurn]
        resourcesAvailable = currentPlayer.resourcesAvailable

        validActions = []

        validActions.extend(self.getBuildingAction(
            1, 1, 0, 0, 0, currentPlayer, resourcesAvailable, self.board.bfsEndpoint, BuildRoad))
        validActions.extend(self.getBuildingAction(1, 1, 1, 1, 0, currentPlayer,
                            resourcesAvailable, self.board.bfsPossibleSettlements, BuildSettlement))

        if resourcesAvailable(0, 0, 0, 2, 3, resourcesAvailable):
            for settlement in currentPlayer.settlements:
                if self.board.nodes[settlement].piece[0] == NodePiece.SETTLEMENT:
                    validActions.append(BuildCity(settlement))

        if self.resourcesAvailable(0, 0, 1, 1, 1, resourcesAvailable):
            validActions.append(DevelopmentCard())

        validActions.extend(self.getPortActions(currentPlayer))

        for devCard in currentPlayer.devCards:
            pass

        validActions.append(EndTurn())

    def getBuildingAction(self, brick, log, sheep, wheat, ore, currentPlayer, resourcesAvailable, func, action):
        if self.resourcesAvailable(brick, log, sheep, wheat, ore, resourcesAvailable):
            valid = set()
            for settlementNodeID in currentPlayer.settlements[0:2]:
                valid.union(set(func(settlementNodeID, self.whoseTurn)))
            return [action(x, self.whoseTurn) for x in valid]
        else:
            return []

    def resourcesAvailable(self, brick, log, sheep, wheat, ore, resourcesAvailable):
        return resourcesAvailable[Resource.BRICK] >= brick and resourcesAvailable[Resource.LOG] >= log and resourcesAvailable[Resource.SHEEP] >= sheep and resourcesAvailable[Resource.WHEAT] >= wheat and resourcesAvailable[Resource.ORE] >= ore

    def getPortActions(self, currentPlayer):
        actions = []

        ports = currentPlayer.getPorts()
        maxTradeQuantity = 3 if Port.THREE_TO_ONE else 4
        inaccessiblePorts = set(
            [Port.BRICK, Port.LOG, Port.ORE, Port.SHEEP, Port.WHEAT]) - ports
        portsToResources = {Port.BRICK: Resource.BRICK, Port.LOG: Resource.LOG,
                            Port.ORE: Resource.ORE, Port.SHEEP: Resource.SHEEP, Port.WHEAT: Resource.SHEEP}
        for port in ports - set([Port.THREE_TO_ONE]):
            resource = portsToResources[port]
            if currentPlayer.resourcesAvailable[resource] >= 2:
                for targetResource in Resource:
                    if targetResource not in [Resource.DESERT, resource]:
                        actions.append(Trade(resource, 2, targetResource))
        for port in inaccessiblePorts - set([Port.THREE_TO_ONE]):
            resource = portsToResources[port]
            if currentPlayer.resourcesAvailable[resource] >= maxTradeQuantity:
                for targetResource in Resource:
                    if targetResource not in [Resource.DESERT, resource]:
                        actions.append(Trade(resource, maxTradeQuantity, targetResource))

        return actions
    
    def getNecessaryActions(self):
        necessaryActionsCopy = self.necessaryActions.copy()
        nextNeededActionEnum = necessaryActionsCopy.pop(0)

        if nextNeededActionEnum == EAction.DISCARD:
            discardActions = []
            currentPlayer = self.playerDataList[self.whoseTurn]
            for resourceID, amount in currentPlayer.resourcesAvailable.items():
                if amount > 0:
                    discardActions.append(Discard(resourceID, necessaryActionsCopy))
            return discardActions
        elif nextNeededActionEnum == EAction.NEXTPLAYER:
            return [NextPlayer(necessaryActionsCopy)]
        elif nextNeededActionEnum == EAction.MOVEROBBER:
            " get all tile id's with other player's settlements and cities"
            " for each player, for each of their settlements/cities's node ids, make a move robber move"
            robbingActions = []

            for tileID, value in self.board.tiles.items():
                for player in self.playerDataList:
                    if len(set(value.nodes) - set(player.settlements)) != len(value.nodes): #player is on this tile
                        robbingActions.append(MoveRobber(tileID, player, necessaryActionsCopy))
            return robbingActions
        elif nextNeededActionEnum == EAction.ROLLDICE:
            return [RollDice(necessaryActionsCopy)]
    
    def isGameOver(self):
        for player in self.playerDataList:
            if player.victoryPoints >= 10:
                return True
        return False


def generateState(agents) -> State:
        board = Board(None, None, None, None).generate_start_board()
        playerList = []
        for i in range(len(agents)):
            playerList.append(PlayerData(agents[i], color=agents[i].color))
        devCards = getDevCardPool()
        state = State(board, playerList, devCards, PlayerColor.BLANK, PlayerColor.BLANK, 0, [])
        return state

def getDevCardPool():
    """
    In the base game, there are 25 development cards: 
        14 knight cards, 
        5 victory point cards, 
        2 road building, 
        2 year of plenty, and 
        2 monopoly.
    """
    devCards = []
    for i in range(0, 14):
        devCards.append(DevCardName.KNIGHT)
    for i in range(0, 2):
        devCards.append(DevCardName.ROAD_BUILDING)
    for i in range(0, 2):
        devCards.append(DevCardName.YEAR_OF_PLENTY)
    for i in range(0, 2):
        devCards.append(DevCardName.MONOPOLY)
    devCards.append(DevCardName.CHAPEL)
    devCards.append(DevCardName.GREAT_HALL)
    devCards.append(DevCardName.LIBRARY)
    devCards.append(DevCardName.MARKET)
    devCards.append(DevCardName.UNIVERSITY)
    return devCards
