# Python 3.8.3

with open("input.txt", "r") as f:
    puzzle_input = [int(i) for i in f.read().split()]


def solve(puzzle):
    for i in puzzle:
        for j in puzzle:
            for k in puzzle:
                if i + j + k == 2020:
                    return i * j * k


print(solve(puzzle_input))
