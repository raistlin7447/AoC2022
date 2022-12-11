from dataclasses import dataclass
import operator
from math import prod

input_file = open("day11_input.txt").read().splitlines()
input_file.append("")

@dataclass
class Monkey:
    items: list[int]
    operation: (str, str, str)
    test: int
    if_true: int
    if_false: int
    inspections: int = 0

    def get_new_worry(self, worry):
        _, oper_string, operand = self.operation
        match oper_string:
            case "+":
                oper = operator.add
            case "*":
                oper = operator.mul

        if operand == "old":
            operand = worry
        else:
            operand = int(operand)

        return oper(worry, operand)

monkeys = []
mod = 1
for _, items, operation, test, if_true, if_false, _ in [input_file[i:i + 7] for i in range(0, len(input_file), 7)]:
    new_monkey = Monkey(
        items=[int(item) for item in items[items.index(":") + 1:].split(",")],
        operation=operation[operation.index("=") + 1:].split(),
        test=int(test[test.index("by") + 2:]),
        if_true=int(if_true[if_true.index("monkey") + 6:]),
        if_false=int(if_false[if_false.index("monkey") + 6:]),
    )
    mod *= new_monkey.test
    monkeys.append(new_monkey)

for _ in range(10000):
    for monkey in monkeys:
        for item in monkey.items:
            monkey.inspections += 1
            new_worry = monkey.get_new_worry(item)
            new_worry %= mod
            if new_worry % monkey.test == 0:
                monkeys[monkey.if_true].items.append(new_worry)
            else:
                monkeys[monkey.if_false].items.append(new_worry)
        monkey.items = []

most_active = sorted([m.inspections for m in monkeys])[-2:]

print(prod(most_active))
