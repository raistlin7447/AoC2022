input = open("day8_input.txt").read().splitlines()
trees = [[j for j in i] for i in input]

height = len(trees)
width = len(trees[0])

answer = 0
for i in range(height):
    for j in range(width):

        # Horizontal
        for r in [range(0, i), range(i+1, width)]:
            for k in r:
                if trees[k][j] >= trees[i][j]:
                    break
            else:
                answer += 1
                break

        # Vertical
        else:
            for r in [range(0, j), range(j+1, height)]:
                for k in r:
                    if trees[i][k] >= trees[i][j]:
                        break
                else:
                    answer += 1
                    break

print(answer)
