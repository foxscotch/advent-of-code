# Python 3.6.1

import re
from timeit import timeit


# Simple dict-based class that sets a default value on missing keys.
class Registers(dict):
    def __missing__(self, key):
        self[key] = 0
        return self[key]


# Class for holding register instructions.
class Instruction:
    instr_re = re.compile(r'(\w+) (inc|dec) (-?\d+) if (\w+ [<>=!]{1,2} -?\d+)')
    cond_re = re.compile(r'(\w+) ([<>=!]{1,2}) (-?\d+)')

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

    def eval_condition_eval(self, regs):
        condition = re.sub(r'([a-z]+)', 'regs[\g<1>]', self.con)
        print(condition)
        return eval(condition)

    def eval_condition_man(self, regs):
        opd, opt, amt = self.cond_re.match(self.con).group(1, 2, 3)
        opd = re.sub(r'([a-z]+)', 'regs[\g<1>]', opd)
        amt = int(amt)
        if opt == '>':
            return regs[opd] > amt
        elif opt == '<':
            return regs[opd] < amt
        elif opt == '>=':
            return regs[opd] >= amt
        elif opt == '<=':
            return regs[opd] <= amt
        elif opt == '==':
            return regs[opd] == amt
        elif opt == '!=':
            return regs[opd] != amt
        else:
            raise ValueError('Invalid condition operator.')


def get_input():
    instructions = []
    with open('input.txt', 'r') as f:
        for line in f:
            instructions.append(Instruction.from_str(line))


def main():
    # instructions = get_input()
    instr = Instruction.from_str('ec dec 631 if bb > 147')



if __name__ == '__main__':
    main()
