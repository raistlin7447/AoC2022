# Part 1
from enum import Enum, IntEnum

rounds = list(map(str.split, open('day2_input.txt').readlines()))

class Shape(Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"

class Outcome(Enum):
    LOST = "X"
    DRAW = "Y"
    WON = "Z"

class OutcomePoints(IntEnum):
    LOST = 0
    DRAW = 3
    WON = 6

class ShapePoints(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

shapes = [Shape.ROCK, Shape.PAPER, Shape.SCISSORS]

points = 0
for opponent, player in rounds:
    opponent_shape = Shape(opponent)
    player_outcome = Outcome(player)
    points += getattr(OutcomePoints, player_outcome.name)

    if player_outcome == Outcome.LOST:
        loser_shape = shapes[(shapes.index(opponent_shape) - 1) % len(shapes)]
        player_shape_points = getattr(ShapePoints, loser_shape.name)

    elif player_outcome == Outcome.DRAW:
        player_shape_points = getattr(ShapePoints, opponent_shape.name)

    else:
        winner_shape = shapes[(shapes.index(opponent_shape) + 1) % len(shapes)]
        player_shape_points = getattr(ShapePoints, winner_shape.name)

    points += player_shape_points

print(points)
