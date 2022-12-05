import re
from collections import deque

input = open("day5_input.txt").readlines()

first_line = input[0]
num_stacks = len(first_line) // 4

stacks = [deque() for i in range(num_stacks)]

for line in input:
    if "[" in line:
        for stack, location in enumerate(range(1, num_stacks * 4, 4)):
            cargo = line[location].strip()
            if cargo:
                stacks[stack].appendleft(cargo)

    elif "move" in line:
        command = re.match(r"move (\d+) from (\d+) to (\d+)\s*", line)
        count, from_stack, to_stack = map(int, command.groups(0))

        for i in range(count):
            cargo = stacks[from_stack - 1].pop()
            stacks[to_stack - 1].append(cargo)

answer = ""
for s in stacks:
    answer += s.pop()

print(answer)
