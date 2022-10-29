from enum import Enum


class DevCardName(Enum):
    KNIGHT = 0
    ROAD_BUILDING = 1
    YEAR_OF_PLENTY = 2
    MONOPOLY = 3
    UNIVERSITY = 4
    MARKET = 5
    GREAT_HALL = 6
    CHAPEL = 7
    LIBRARY = 8


class DevCard:

    def __init__(self, name, action) -> None:
        self.name = name
        self.action = action
