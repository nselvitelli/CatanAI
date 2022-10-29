from Actions.Action import Action
from Board import Board
from Resource import Resource
from PlayerData import PlayerData
from State import State
import random


class MoveRobber(Action):

    def __init__(self, tileID, stealPlayer) -> None:
        super().__init__()
        self.tileID = tileID
        self.stealPlayer = stealPlayer

    def apply(self, state):
        board = Board(state.board.tiles, state.board.nodes,
                      state.board.edges, self.tileID)

        stealData = state.playerDataDict[self.stealPlayer]

        totalResourceCount = stealData.getTotalResources()

        stealNum = random.randint(1, totalResourceCount)

        count = 0
        takeResource = Resource.WHEAT
        for key in stealData.resourcesAvailable:
            if count + stealData.resourcesAvailable[key] >= stealNum:
                takeResource = key
                break
            count += stealData.resourcesAvailable[key]

        # need to generate new playerData
        newPlayerDataDict = {}
        for key in state.playerDataDict:
            oldPlayerData = state.playerDataDict[key]
            if key == self.stealPlayer:
                newResources = {}
                for resource in oldPlayerData.resourcesAvailable:
                    if resource == takeResource:
                        newResources[resource] = oldPlayerData.resourcesAvailable[resource] - 1
                    else:
                        newResources[resource] = oldPlayerData.resourcesAvailable[resource]
                newPlayerDataDict[key] = PlayerData(oldPlayerData.victoryPoints, oldPlayerData.devCards,
                                                    oldPlayerData.settlements, newResources, oldPlayerData.armySize, oldPlayerData.color)
                pass
            elif key == state.whoseTurn:
                newResources = {}
                for resource in oldPlayerData.resourcesAvailable:
                    if resource == takeResource:
                        newResources[resource] = oldPlayerData.resourcesAvailable[resource] + 1
                    else:
                        newResources[resource] = oldPlayerData.resourcesAvailable[resource]
                newPlayerDataDict[key] = PlayerData(oldPlayerData.victoryPoints, oldPlayerData.devCards,
                                                    oldPlayerData.settlements, newResources, oldPlayerData.armySize, oldPlayerData.color)
            else:
                newResources = {}
                for resource in oldPlayerData.resourcesAvailable:
                    newResources[resource] = oldPlayerData.resourcesAvailable[resource]
                newPlayerDataDict[key] = PlayerData(oldPlayerData.victoryPoints, oldPlayerData.devCards,
                                                    oldPlayerData.settlements, newResources, oldPlayerData.armySize, oldPlayerData.color)

        return State(board, newPlayerDataDict, state.devCards, state.longestRoad, state.largestArmy, state.whoseTurn)
