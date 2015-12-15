with open('input.txt', 'r') as f:
    puzzle_input = f.read()


current_floor = 0

for paren in puzzle_input:
    if paren == '(':
        current_floor += 1
    elif paren == ')':
        current_floor -= 1

print(current_floor)


# My answer: 74
