# Part 1
from enum import Enum, IntEnum

rounds = list(map(str.split, open('day2_input.txt').readlines()))

class Shape(Enum):
    ROCK = "ROCK"
    A = ROCK
    X = ROCK

    PAPER = "PAPER"
    B = PAPER
    Y = PAPER

    SCISSORS = "SCISSORS"
    C = SCISSORS
    Z = SCISSORS

    def __lt__(self, other):
        if self == self.ROCK and other == self.PAPER:
            return True
        if self == self.PAPER and other == self.SCISSORS:
            return True
        if self == self.SCISSORS and other == self.ROCK:
            return True
        return False

    def __gt__(self, other):
        if self == self.ROCK and other == self.SCISSORS:
            return True
        if self == self.SCISSORS and other == self.PAPER:
            return True
        if self == self.PAPER and other == self.ROCK:
            return True
        return False


class OutcomePoints(IntEnum):
    LOST = 0
    DRAW = 3
    WON = 6

class ShapePoints(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

points = 0
for opponent, player in rounds:
    opponent_shape = getattr(Shape, opponent)
    player_shape = getattr(Shape, player)
    player_shape_points = getattr(ShapePoints, player_shape.value)

    points += player_shape_points

    if opponent_shape == player_shape:
        points += OutcomePoints.DRAW

    elif opponent_shape < player_shape:
        points += OutcomePoints.WON

    else:
        points += OutcomePoints.LOST

print(points)
