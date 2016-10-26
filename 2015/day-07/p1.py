board = None


# god, this is so overkill

class Board:
    def __init__(self, file):
        self.instructions = []
        self.wires = WireManager()

        for line in file:
            tokens = [int(i) if i.isdigit() else i for i in line.split(' ')]
            self.instructions.append(Instruction(tokens))

        for instr in self.instructions:
            for op in instr['operands']:
                if type(op) is str:
                    self.wires.add_wire(op)

    def run(self):
        skipped = False

        for instr in instructions:
            if not instr.is_runnable():
                skipped = True
            else:
                instr.run()
            
        if skipped:
            self.run()


class WireManager:
    def __init__(self):
        self.wires = {}

    def add_wire(self, wire):
        self.wires[wire.name] = wire
        wire.manager = self

    def get_wire(self, wire):
        return self.wires[wire].value

    def set_wire(self, wire, value):
        self.wires[wire].value = value

    def check_runnable(self, *wires):
        for wire in wires:
            if type(wire) != int and self.wires[wire] == None:
                return False
        return True


class Wire:
    def __init__(self, name):
        self.name = name
        self.value = None
        self.manager = None


class Instruction:
    def __init__(self, board, tokens):
        if len(tokens) == 4:
            self.operator = 'NOT'
            self.operands = [tokens[1]]
        elif len(tokens) == 5:
            self.operator = tokens[1]
            self.operands = [tokens[0], tokens[2]]
        else:
            self.operator = 'ASSIGN'
            self.operands = tokens[0]
        self.dest = tokens[-1]

    def is_runnable():
        return self.board.wires.check_runnable(*self.operands)

    def run():
        operands = []

        for op in self.operands:
            if type(op) != int:
                operands.append(self.board.wires.get_wire(op))
            else:
                operands.append(op)

        elif instr['operator'] == 'NOT':
            self.board.wires.set_wire(self.dest, operands[0])
        elif instr['operator'] == 'LSHIFT':
            pass
        elif instr['operator'] == 'RSHIFT':
            pass
        elif instr['operator'] == 'AND':
            pass
        elif instr['operator'] == 'OR':
            pass
        else:
            # ASSIGN
            pass


with open('input.txt', 'r') as file:
    board = Board(file)


board.run()
print(board.wires.get_wire('a'))
