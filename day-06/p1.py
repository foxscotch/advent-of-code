import re
from numpy import matrix


instructions = []

with open('input.txt', 'r') as f:
    regex = re.compile(r'([\w ]+) (\d+),(\d+) .+ (\d+),(\d+)')
    for line in f:
        match = regex.match(line)
        instructions.append((
            match.group(1),
            (int(match.group(2)), int(match.group(3))),
            (int(match.group(3)), int(match.group(5)))
        ))

lights = matrix([[0 for i in range(1000)] for j in range(1000)])

def act(instruction):
    action = instruction[0]
    x1, y1 = instruction[1]
    x2, y2 = instruction[2]

    if action == 'turn on':
        lights[x1:x2, y1:y2] = 1
    elif action == 'turn off':
        lights[x1:x2, y1:y2] = 0
    else:
        lights[x1:x2, y1:y2] ^= 1

for step in instructions:
    act(step)

print(lights.flatten().tolist()[0].count(1))
