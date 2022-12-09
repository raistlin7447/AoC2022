import math
from copy import copy
from dataclasses import dataclass


in_file = open("day9_input.txt").read().splitlines()
steps = [(direction, int(distance)) for direction, distance in [line.split() for line in in_file]]


@dataclass
class Point:
    X: int
    Y: int

    def __iter__(self):
        yield self.X
        yield self.Y

    def __copy__(self):
        return Point(self.X, self.Y)

    def move_right(self):
        self.X += 1

    def move_left(self):
        self.X -= 1

    def move_up(self):
        self.Y -= 1

    def move_down(self):
        self.Y += 1


start_location = Point(0, 4)
num_knots = 10

rope = []
for i in range(num_knots):
    rope.append(copy(start_location))

head_location = rope[0]
tail_location = rope[-1]
tail_visited = {str(head_location)}


def move_knot(head, tail):
    distance = math.dist(head, tail)
    if distance > 1.5:
        if head.Y > tail.Y:
            tail.move_down()
        elif head.Y < tail.Y:
            tail.move_up()

        if head.X > tail.X:
            tail.move_right()
        elif head.X < tail.X:
            tail.move_left()


for direction, distance in steps:
    for move in range(distance):
        match direction:
            case "R":
                head_location.move_right()
            case "L":
                head_location.move_left()
            case "U":
                head_location.move_up()
            case "D":
                head_location.move_down()

        for knot in range(len(rope)-1):
            move_knot(rope[knot], rope[knot+1])

        tail_visited.add(str(tail_location))

print(len(tail_visited))
