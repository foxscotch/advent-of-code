# Python 3.6.1

import re


"""Simple dict-based class that sets a default value on missing keys."""
class Registers(dict):
    def __missing__(self, key):
        self[key] = 0
        return self[key]


"""Class for holding register instructions."""
class Instruction:
    instr_re = re.compile(r'(\w+) (inc|dec) (-?\d+) if (\w+ [<>=!]{1,2} -?\d+)')
    repl_re = re.compile(r'')

    def __init__(operand, operation, amount, condition):
        self.opd = operand
        self.opt = operation
        self.amt = amount
        self.con = condition

    @classmethod
    def from_str(cls, s, reg_var=None):
        match = cls.instr_re.match(s)
        operand = match.group(1)
        operation = match.group(2)
        amount = int(match.group(3))
        if reg_var is not None:
            condition = re.sub(r'.+if (\w+)', f'{reg_var}[\g<1>]', s)
        else:
            condition = match.group(4)
        return cls(operand, operation, amount, condition)


def get_input():
    with open('input.txt', 'r') as f:


def main():
    instructions = get_input()


if __name__ == '__main__':
    main()
