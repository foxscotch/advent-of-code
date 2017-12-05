# Python 3.6.1 / Official

with open('input.txt', 'r') as f:
    puzzle_input = []
    for line in f:
        puzzle_input.append(int(line))

i = 0
steps = 0
while True:
    offset = puzzle_input[i]
    puzzle_input[i] += -1 if offset >= 3 else 1
    i += offset
    steps += 1
    if i < 0 or i >= len(puzzle_input):
        break

print(steps)
