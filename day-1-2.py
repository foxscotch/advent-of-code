with open('day-1-input.txt', 'r') as f:
    puzzle_input = f.read()


current_floor = 0
current_position = 0

for paren in puzzle_input:
    current_position += 1

    if paren == '(':
        current_floor += 1
    elif paren == ')':
        current_floor -= 1

    if current_floor < 0:
        break

print(current_position)


# My answer: 1795
