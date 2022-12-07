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

answer = 0
for directory, size in directories.items():
    if size <= 100000:
        answer += size

print(answer)
