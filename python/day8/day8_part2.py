input = open("day8_input.txt").read().splitlines()
trees = [[j for j in i] for i in input]

height = len(trees)
width = len(trees[0])

answer = 0
for i in range(height):
    for j in range(width):
        score = 1

        # Horizontal
        for r in [reversed(range(0, i)), range(i+1, width)]:
            seen = 0
            for k in r:
                seen += 1
                if trees[k][j] >= trees[i][j]:
                    break
            score *= seen

        # Vertical
        for r in [reversed(range(0, j)), range(j+1, height)]:
            seen = 0
            for k in r:
                seen += 1
                if trees[i][k] >= trees[i][j]:
                    break
            score *= seen

        if score > answer:
            answer = score

print(answer)
