# Python 3.6.1

import re


with open("input.txt", "r") as f:
    puzzle_input = []
    for line in f:
        puzzle_input.append([int(i) for i in re.split("\s", line)[:-1]])

total = 0
for row in puzzle_input:
    for dividend in row:
        for divisor in row:
            if dividend > divisor and dividend % divisor == 0:
                total += dividend // divisor

print(total)
