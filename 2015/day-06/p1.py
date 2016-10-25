import re
from numpy import matrix


instructions = []

with open('input.txt', 'r') as f:
    regex = re.compile(r'([\w ]+) (\d+),(\d+) .+ (\d+),(\d+)')
    for line in f:
        action, x1, y1, x2, y2 = regex.match(line).groups()
        instructions.append((
            action,
            (int(x1), int(y1)),
            (int(x2), int(y2))
        ))

lights = matrix([[0 for i in range(1000)] for j in range(1000)])

def act(instruction):
    action = instruction[0]
    x1, y1 = instruction[1]
    x2, y2 = instruction[2]
    x2 += 1
    y2 += 1

    if action == 'turn on':
        lights[x1:x2, y1:y2] = 1
    elif action == 'turn off':
        lights[x1:x2, y1:y2] = 0
    else:
        lights[x1:x2, y1:y2] ^= 1

# The e stands for "easy"
def selection_size_e(instruction):
    x1, y1 = instruction[1]
    x2, y2 = instruction[2]
    x2 += 1
    y2 += 1

    return lights[x1:x2, y1:y2].flatten().tolist()[0].count(0)

# The m stands for "manual"
def selection_size_m(instruction):
    x1, y1 = instruction[1]
    x2, y2 = instruction[2]
    x2 += 1
    y2 += 1

    width = x2 - x1
    height = y2 - y1
    return width * height

for step in instructions:
    act(step)

print(lights.flatten().tolist()[0].count(1))
