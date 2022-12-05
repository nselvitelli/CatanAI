from Actions.Action import Action, EAction
from Actions.MoveRobber import MoveRobber
from PlayerColor import PlayerColor
from DevCard import DevCardName

# Action class for playing a knight


class Knight(Action):

    def __init__(self, debug=False) -> None:
        super().__init__(debug)

    def apply(self, state):
        newState = state.getCopy()

        newState.necessaryActions.insert(0, EAction.MOVEROBBER)
        
        playerTurnData = newState.playerDataList[newState.whoseTurn]
        playerTurnData.armySize += 1
        playerTurnData.devCards.remove(DevCardName.KNIGHT)

        playerTurnData.devCardsUsed += 1


        # corrects largest army if necessary

        # state.largestArmy is an index, -1 if no one has it yet
        previousLargestArmyPlayer = newState.playerDataList[newState.largestArmy] if newState.largestArmy != -1 else None
        largestArmyPlayer = None if newState.largestArmy == -1 else newState.playerDataList[newState.largestArmy]
        largestIdx = -1
        maxKnights = largestArmyPlayer.armySize if largestArmyPlayer != None else 0

        for idx, player in enumerate(newState.playerDataList):
            if player.armySize > maxKnights:
                maxKnights = player.armySize
                largestArmyPlayer = player
                largestIdx = idx
        
        if maxKnights >= 3 and previousLargestArmyPlayer != largestArmyPlayer:
            if previousLargestArmyPlayer != None:
                previousLargestArmyPlayer.victoryPoints -= 2
            if largestArmyPlayer != None:
                largestArmyPlayer.victoryPoints += 2
            newState.largestArmy = largestIdx
            
        return newState

    # remove card from player hand

    def getActionAsString(self):
            return "Play Knight DevCard"