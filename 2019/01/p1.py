# Python 3.8.3

with open("input.txt", "r") as f:
    puzzle_input = [int(i) for i in f.read().split()]


def fuel_needed(mass):
    return mass // 3 - 2


sum = 0

for mass in puzzle_input:
    sum += fuel_needed(mass)

print(sum)
