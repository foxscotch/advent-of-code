# Python 3.6.1

with open('input.txt', 'r') as f:
    puzzle_input = [int(i) for i in f.read()[0:-1]]

total = 0
puzzle_inputc = len(puzzle_input) // 2
for cur_index in range(len(puzzle_input)):
    current = puzzle_input[cur_index]
    pnext = puzzle_input[(cur_index + puzzle_input) % len(puzzle_input)]

    if current == pnext:
        total += current

print(total)
