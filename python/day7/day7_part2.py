from collections import defaultdict
from pathlib import Path

input = open("day7_input.txt").read().splitlines()

directories = defaultdict(int)
current_directory = Path("/")

for line in input:
    match line.split():
        case ["$", "cd", directory]:
            current_directory = (current_directory / Path(directory)).resolve()
        case ["$", "ls"]:
            pass
        case ["dir", directory]:
            pass
        case [size, file_name]:
            walk = Path("/")
            for part in current_directory.parts:
                walk /= Path(part)
                directories[walk] += int(size)

needed_space = 30000000 - (70000000 - directories[Path("/").resolve()])
answer = 70000000
for directory, size in directories.items():
    if needed_space <= size < answer:
        answer = size

print(answer)
