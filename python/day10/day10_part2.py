from dataclasses import dataclass

input_file = open("day10_input.txt").read().splitlines()


@dataclass
class CPU:
    x_reg: int = 0
    cycle: int = 0
    operation: str = ""
    operand: int = 0
    execution_counter: int = 0

    def set_operation(self, command):
        match command.split():
            case ["noop"]:
                self.operation = "noop"
                self.operand = 0
                self.execution_counter = 1
            case ["addx", operand]:
                self.operation = "addx"
                self.operand = int(operand)
                self.execution_counter = 2

    def run_cycle(self):
        self.cycle += 1
        self.execution_counter -= 1
        match self.operation:
            case "addx":
                if self.execution_counter == 0:
                    self.x_reg += self.operand


cpu = CPU(x_reg=1)
row = 0
for command in input_file:
    cpu.set_operation(command)
    while cpu.execution_counter > 0:
        column = cpu.cycle - (row * 40)

        if column in [cpu.x_reg - 1, cpu.x_reg, cpu.x_reg + 1]:
            print("#", end="")
        else:
            print(".", end="")

        if (cpu.cycle+1) % 40 == 0:
            row += 1
            print()

        cpu.run_cycle()
