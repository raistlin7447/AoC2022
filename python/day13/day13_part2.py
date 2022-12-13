from functools import cmp_to_key

input_file = open("day13_input.txt").read().split()
packets = [eval(i) for i in input_file]
packets.append([[2]])
packets.append([[6]])

def compare_items(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        elif left > right:
            return -1
        else:
            return 0
    elif isinstance(left, list) and isinstance(right, list):
        try:
            for i in range(max(len(left), len(right))):
                result = compare_items(left[i], right[i])
                if result == 0:
                    continue
                return result

        except IndexError:
            if len(left) < len(right):
                return 1
            elif len(left) > len(right):
                return -1
        return 0
    else:
        if isinstance(left, int):
            return compare_items([left], right)
        else:
            return compare_items(left, [right])

packets.sort(key=cmp_to_key(compare_items), reverse=True)

divider_1 = packets.index([[2]]) + 1
divider_2 = packets.index([[6]]) + 1

print(divider_1 * divider_2)
