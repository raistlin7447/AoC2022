pairs = list(map(lambda x: x.strip().split(","), open("day4_input.txt")))

overlaps = 0
for e1, e2 in pairs:
    e1_start, e1_end = map(int, e1.split("-"))
    e1_assignments = set(range(e1_start, e1_end + 1))

    e2_start, e2_end = map(int, e2.split("-"))
    e2_assignments = set(range(e2_start, e2_end + 1))

    if e1_assignments & e2_assignments:
        overlaps += 1

print(overlaps)
