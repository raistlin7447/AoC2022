badges = []

rucksacks = list(map(str.strip, open("day3_input.txt").readlines()))

for r1, r2, r3 in [rucksacks[i:i + 3] for i in range(0, len(rucksacks), 3)]:
    badge = (set(r1) & set(r2) & set(r3)).pop()
    badges.append(badge)

total = 0
for item in badges:
    if item.isupper():
        total += ord(item) - 38
    else:
        total += ord(item) - 96

print(total)
