# Python 3.6.1

with open('input.txt', 'r') as f:
    puzzle_input = []
    for line in f:
        puzzle_input.append(int(line))

i = 0
steps = 0
while True:
    puzzle_input[i] += 1
    i += puzzle_input[i] - 1
    steps += 1
    if i < 0 or i >= len(puzzle_input):
        break

print(steps)
