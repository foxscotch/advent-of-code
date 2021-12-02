# Python 3.6.1

from collections import defaultdict


with open("input.txt", "r") as f:
    puzzle_input = f.read().split()

two_of_same_letter = 0
three_of_same_letter = 0


def difference(id1, id2):
    count = 0
    for a, b in zip(id1, id2):
        if a != b:
            count += 1
    return count


def main():
    for id1 in puzzle_input:
        for id2 in puzzle_input:
            if difference(id1, id2) == 1:
                return id1, id2


answer = ""
for a, b in zip(*main()):
    if a == b:
        answer += a

print(answer)
