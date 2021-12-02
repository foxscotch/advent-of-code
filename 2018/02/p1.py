# Python 3.6.1

from collections import defaultdict


with open("input.txt", "r") as f:
    puzzle_input = f.read().split()

two_of_same_letter = 0
three_of_same_letter = 0


def appearances(id):
    counts = defaultdict(lambda: 0)
    for char in id:
        counts[char] += 1
    return 2 in counts.values(), 3 in counts.values()


for id in puzzle_input:
    twos, threes = appearances(id)
    if twos:
        two_of_same_letter += 1
    if threes:
        three_of_same_letter += 1

print(two_of_same_letter * three_of_same_letter)
