# Python 3.6.1

with open("input.txt", "r") as f:
    puzzle_input = [int(i) for i in f.read()[0:-1]]

total = 0
for cur_index in range(len(puzzle_input)):
    next_index = cur_index + 1 if not cur_index == len(puzzle_input) - 1 else 0
    puz_cur = puzzle_input[cur_index]
    pnext = puzzle_input[next_index]

    if puz_cur == pnext:
        total += puz_cur

print(total)
