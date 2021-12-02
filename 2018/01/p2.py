# Python 3.6.1

from collections import deque
from itertools import cycle


with open("input.txt", "r") as f:
    puzzle_input = [int(i) for i in f.read().split()]


def main():
    frequencies = set()
    freq = 0

    for i in cycle(puzzle_input):
        if freq in frequencies:
            return freq
        frequencies.add(freq)
        freq += i


print(main())
