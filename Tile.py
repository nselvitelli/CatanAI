

from mimetypes import init


class Tile:

    def __init__(self, number, resource, nodes) -> None:
        self.number = number
        self.resource = resource
        self.nodes = nodes

    def getCopy(self):
        newNodes = []
        for node in self.nodes:
            newNodes.append(node)
        return Tile(self.number, self.resource, newNodes)
