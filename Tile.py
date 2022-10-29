

from mimetypes import init

"""
Tile is referenced by each neighboring Node

- Tile has a reference to each node that borders it (bc robber)
- has a number value based on the dice roll
- has a resource enum to say what value to produce
- isBlockedByRobber changes when robber moves around tile

"""
class Tile:

    def __init__(self, number, resource, nodes) -> None:
        self.number = number
        self.resource = resource
        self.isBlockedByRobber = False
        self.nodes = nodes


