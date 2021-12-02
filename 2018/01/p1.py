# Python 3.6.1

with open("input.txt", "r") as f:
    puzzle_input = [int(i) for i in f.read().split()]

print(sum(puzzle_input))
