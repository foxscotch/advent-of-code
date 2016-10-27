# god, this is so overkill

class Board:
    def __init__(self, file):
        self.instructions = []
        self.wires = WireManager()

        for line in file:
            tokens = [int(i) if i.isdigit() else i.strip() for i in line.split(' ')]
            self.instructions.append(Instruction(self, tokens))

        for instr in self.instructions:
            for op in instr.operands:
                if type(op) is str:
                    self.wires.add_wire(op)
            self.wires.add_wire(instr.dest)

    def run(self):
        skipped = False

        for instr in self.instructions:
            if instr.is_runnable():
                instr.run()
            else:
                skipped = True
            
        if skipped:
            self.run()


class WireManager:
    def __init__(self):
        self._wires = {}

    def add_wire(self, wire):
        wire = Wire(wire)
        self._wires[wire.name] = wire
        wire.manager = self

    def get_wire(self, wire):
        return self._wires[wire].value

    def set_wire(self, wire, value):
        self._wires[wire].value = value

    def check_runnable(self, *wires):
        for wire in wires:
            if type(wire) is not int and self.get_wire(wire) is None:
                return False
        return True


class Wire:
    def __init__(self, name):
        self.name = name
        self.value = None
        self.manager = None

    def __str__(self):
        return '{}={}'.format(self.name, self.value)


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
            self.operands = [tokens[0]]
        self.dest = tokens[-1]
        self.board = board

    def is_runnable(self):
        return self.board.wires.check_runnable(*self.operands)

    def run(self):
        operands = []

        for op in self.operands:
            if type(op) != int:
                operands.append(self.board.wires.get_wire(op))
            else:
                operands.append(op)

        if self.operator == 'NOT':
            self.board.wires.set_wire(self.dest, ~operands[0])
        elif self.operator == 'LSHIFT':
            self.board.wires.set_wire(self.dest, operands[0] << operands[1])
        elif self.operator == 'RSHIFT':
            self.board.wires.set_wire(self.dest, operands[0] >> operands[1])
        elif self.operator == 'AND':
            self.board.wires.set_wire(self.dest, operands[0] & operands[1])
        elif self.operator == 'OR':
            self.board.wires.set_wire(self.dest, operands[0] | operands[1])
        else:
            # ASSIGN
            self.board.wires.set_wire(self.dest, operands[0])


with open('input.txt', 'r') as file:
    board = Board(file)


board.run()
print(board.wires.get_wire('a'))
