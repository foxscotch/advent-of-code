# Python 3.8.3

from collections import defaultdict

with open('input.txt', 'r') as f:
    puzzle_input = [int(i) for i in f.read().split()]

def solve(puzzle):
    for i in puzzle:
        for j in puzzle:
            if i + j == 2020:
                return i * j

print(solve(puzzle_input))
