from collections import deque

input = open("day6_input.txt").readline()

window_size = 14
window = deque(input[:window_size], maxlen=window_size)
for i, char in enumerate(input[window_size:]):
    window.append(char)
    if len(window) == len(set(window)):
        print(i+window_size+1)
        break
