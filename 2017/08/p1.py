# Python 3.6.1

import re
from timeit import timeit


class Registers(dict):
    """Simple dict-based class that sets a default value on missing keys."""

    def __missing__(self, key):
        self[key] = 0
        return self[key]


class Instruction:
    """Class for holding register instructions."""

    instr_re = re.compile(r"(\w+) (inc|dec) (-?\d+) if (\w+ [<>=!]{1,2} -?\d+)")
    cond_re = re.compile(r"(\w+) ([<>=!]{1,2}) (-?\d+)")

    def __init__(self, operand, operation, amount, condition):
        self.opd = operand
        self.opt = operation
        self.amt = amount
        self.con = condition

    @classmethod
    def from_str(cls, s):
        match = cls.instr_re.match(s)
        operand = match.group(1)
        operation = match.group(2)
        amount = int(match.group(3))
        condition = match.group(4)
        return cls(operand, operation, amount, condition)

    def eval_operation(self, regs):
        if self.eval_condition(regs):
            if self.opt == "inc":
                regs[self.opd] += self.amt
            elif self.opt == "dec":
                regs[self.opd] -= self.amt
            else:
                raise ValueError("Invalid operation.")

    def eval_condition(self, regs):
        opd, opt, amt = self.cond_re.match(self.con).group(1, 2, 3)
        amt = int(amt)
        if opt == ">":
            return regs[opd] > amt
        elif opt == "<":
            return regs[opd] < amt
        elif opt == ">=":
            return regs[opd] >= amt
        elif opt == "<=":
            return regs[opd] <= amt
        elif opt == "==":
            return regs[opd] == amt
        elif opt == "!=":
            return regs[opd] != amt
        else:
            raise ValueError("Invalid condition operator.")

    def eval_condition_eval(self, regs):
        """
        This function does the same thing as eval_condition, but using eval()
        instead of manually checking the comparison operators. With timeit, I
        determined that the manual version takes about 40% of the time this one
        does, but I wanted to keep it here for posterity.
        """
        condition = re.sub(r"([a-z]+)", 'regs["\g<1>"]', self.con)
        return eval(condition)


def get_input():
    instructions = []
    with open("input.txt", "r") as f:
        for line in f:
            instructions.append(Instruction.from_str(line))
    return instructions


def main():
    instructions = get_input()
    regs = Registers()

    for instr in instructions:
        instr.eval_operation(regs)

    print(max(regs.values()))

    # Timing code:
    # instr = Instruction.from_str('ec dec 631 if bb != 147')
    # print(f'Manually: {timeit(lambda: instr.eval_condition(regs))}')
    # print(f'Using eval: {timeit(lambda: instr.eval_condition_eval(regs))}')


if __name__ == "__main__":
    main()
