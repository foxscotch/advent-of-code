# Python 3.6.1 / Official

import re


with open('input.txt', 'r') as f:
    puzzle_input = []
    for line in f:
      puzzle_input.append([int(i) for i in re.split('\s', line)[:-1]])

total = 0
for row in puzzle_input:
  total += max(row) - min(row)

print(total)
