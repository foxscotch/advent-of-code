# Python 3.8.3

with open("input.txt", "r") as f:
    puzzle_input = [int(i) for i in f.read().split(",")]
    puzzle_input[1] = 12
    puzzle_input[2] = 2


def solve(puzzle):
    puzzle = puzzle.copy()
    position = 0

    while True:
        if position > len(puzzle):
            break

        opcode = puzzle[position]
        left = puzzle[position + 1]
        right = puzzle[position + 2]
        dest = puzzle[position + 3]

        if opcode == 1:
            result = puzzle[left] + puzzle[right]
        elif opcode == 2:
            result = puzzle[left] * puzzle[right]
        else:
            break  # end reading if opcode is 99

        puzzle[dest] = result

        position += 4

    return puzzle


print(solve(puzzle_input)[0])
