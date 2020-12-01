# Python 3.8.3

with open('input.txt', 'r') as f:
    puzzle_input = [int(i) for i in f.read().split()]

def fuel_needed(mass):
    fuel = mass // 3 - 2
    return fuel + fuel_needed(fuel) if fuel > 0 else 0

sum = 0

for mass in puzzle_input:
    sum += fuel_needed(mass)

print(sum)
