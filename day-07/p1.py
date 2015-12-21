import re


instructions = []

with open('input.txt', 'r') as f:
    regex = re.compile(r'([a-z]*) ?(NOT|OR|AND|RSHIFT|LSHIFT)? ?([a-z]*) ?(\d*) -> ([a-z]+)')
    for line in f:
        match = regex.match(line)
        instr_dict = {
            'operand_l': match.group(1),
            'op': match.group(2),
            'operand_r': match.group(3),
            'number': match.group(4),
            'target': match.group(5)
        }
        instructions.append(instr_dict)

print(instructions)