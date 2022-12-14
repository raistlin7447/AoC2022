input_file = open("day14_input.txt").read().splitlines()

rocks = set()
bottom = 0

for line in input_file:
    points = [list(map(int, point.split(","))) for point in line.split(" -> ")]
    for point1, point2 in zip(points, points[1:]):
        if point2[0] < point1[0]:
            point1_x, point2_x = point2[0], point1[0]
        else:
            point1_x, point2_x = point1[0], point2[0]

        if point2[1] < point1[1]:
            point1_y, point2_y = point2[1], point1[1]
        else:
            point1_y, point2_y = point1[1], point2[1]

        for i in range(point1_x, point2_x + 1):
            for j in range(point1_y, point2_y + 1):
                rocks.add((i, j))
                if j + 1 > bottom:
                    bottom = j + 1

cycles = 0
done = False

while not done:
    sand_location = (500, 0)
    while True:
        if sand_location[1] >= bottom:
            done = True
            break

        down = (sand_location[0], sand_location[1] + 1)
        diag_left = (sand_location[0] - 1, sand_location[1] + 1)
        diag_right = (sand_location[0] + 1, sand_location[1] + 1)

        for direction in [down, diag_left, diag_right]:
            if direction not in rocks:
                sand_location = direction
                break
        else:
            rocks.add(sand_location)
            cycles += 1
            break

print(cycles)
