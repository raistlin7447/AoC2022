common_items = []

for rucksack in open("day3_input.txt").readlines():
    size = len(rucksack)
    c1 = set(rucksack[:size // 2])
    c2 = set(rucksack[size // 2:])
    common_items.append((c1 & c2).pop())

total = 0
for item in common_items:
    if item.isupper():
        total += ord(item) - 38
    else:
        total += ord(item) - 96

print(total)
