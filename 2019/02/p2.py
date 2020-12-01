# Python 3.8.3

with open('input.txt', 'r') as f:
    puzzle_input = [int(i) for i in f.read().split(',')]

def solve(puzzle, noun, verb):
    puzzle = puzzle.copy()
    puzzle[1] = noun
    puzzle[2] = verb
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

def solve_for(puzzle, desired_output):
    for i in range(100):
        for j in range(100):
            if solve(puzzle, i, j)[0] == desired_output:
                return i, j

noun, verb = solve_for(puzzle_input, 19690720)
print(100 * noun + verb)
