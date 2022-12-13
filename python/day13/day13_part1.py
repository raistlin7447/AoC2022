input_file = open("day13_input.txt").read().split("\n\n")

pairs = [(eval(i), eval(j)) for i, j in [pairs.split() for pairs in input_file]]

def compare_items(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        elif left > right:
            return False
        else:
            return None
    elif isinstance(left, list) and isinstance(right, list):
        try:
            for i in range(max(len(left), len(right))):
                result = compare_items(left[i], right[i])
                if result is None:
                    continue
                return result

        except IndexError:
            if len(left) < len(right):
                return True
            elif len(left) > len(right):
                return False
        return None
    else:
        if isinstance(left, int):
            return compare_items([left], right)
        else:
            return compare_items(left, [right])

answer = 0
for i, pairs in enumerate(pairs, start=1):
    result = compare_items(pairs[0], pairs[1])
    if result:
        answer += i

print(answer)
