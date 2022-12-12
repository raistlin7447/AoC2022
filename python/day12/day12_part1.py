import math
from copy import copy
from dataclasses import dataclass, field

input_file = open("day12_input.txt").read().splitlines()

grid = []
start_node = None
end_node = None


@dataclass
class Cell:
    location: tuple
    #parent: tuple = field(compare=False, default=None)
    height: int = field(compare=False, default=None)
    g: int = field(compare=False, default=math.inf)
    h: int = field(compare=False, default=math.inf)
    f: int = field(compare=False, default=math.inf)

    def get_neighbors(self):
        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x = self.location[0] + i
            new_y = self.location[1] + j

            if 0 <= new_x < grid_height and 0 <= new_y < grid_width:
                neighbor = copy(grid[new_x][new_y])
                if neighbor.height < self.height or neighbor.height in [self.height, self.height + 1]:
                    yield neighbor

    def get_h(self):
        return abs(self.location[0] - end_node.location[0]) + abs(self.location[1] - end_node.location[1])

    def __eq__(self, other):
        return self.location == other.location


for i, line in enumerate(input_file):
    row = []
    for j, item in enumerate(line):
        location = (i, j)
        height = ord(item) - 96
        match item:
            case "S":
                start_node = Cell(location=location, height=1, g=0, f=0)
                row.append(start_node)
            case "E":
                end_node = Cell(location=location, height=26)
                row.append(end_node)
            case _:
                row.append(Cell(location=location, height=height))

    grid.append(row)

grid_height = len(grid)
grid_width = len(grid[0])

open_nodes = [start_node]
closed_nodes = []

done = False
while open_nodes and not done:
    open_nodes = sorted(open_nodes, key=lambda x: x.f, reverse=True)
    node = open_nodes.pop()

    for neighbor in node.get_neighbors():
        neighbor.g = node.g + 1
        neighbor.h = neighbor.get_h()
        neighbor.f = neighbor.g + neighbor.h

        if neighbor == end_node:
            done = neighbor
            break

        try:
            neighbor_open_location = open_nodes.index(neighbor)
            if neighbor_open_location:
                if open_nodes[neighbor_open_location].f <= neighbor.f:
                    continue
        except ValueError:
            pass

        try:
            neighbor_closed_location = closed_nodes.index(neighbor)
            if neighbor_closed_location:
                if closed_nodes[neighbor_closed_location].f <= neighbor.f:
                    continue
        except ValueError:
            pass

        open_nodes.append(neighbor)
    closed_nodes.append(node)

print(done)
