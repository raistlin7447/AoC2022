# Part 1
with open('day1_input.txt') as f:
    elves = []
    elf_number = 0
    elf_total = 0

    for l in f.readlines():
        if not l.strip():
            elves.append(elf_total)
            elf_number += 1
            elf_total = 0
        else:
            elf_total += int(l)

    elves.append(elf_total)

    print(max(elves))
