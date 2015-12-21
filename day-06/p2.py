import re
from numpy import matrix, uint32


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
        lights[x1:x2, y1:y2] += 1
    elif action == 'turn off':
        lights[x1:x2, y1:y2] -= 1
        lights[lights < 0] = 0
    else:
        lights[x1:x2, y1:y2] += 2

for step in instructions:
    act(step)

result_list = lights.flatten().tolist()[0]
print(sum([item for item in result_list if item > 0]))
