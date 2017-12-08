# Python 3.6.1

with open('input.txt', 'r') as f:
    puzzle_input = []
    for line in f:
        puzzle_input.append(line.strip().split(' '))

total = 0
for phrase in puzzle_input:
    bad = False
    for word in phrase:
        if phrase.count(word) > 1:
            bad = True
            break
    if not bad:
        total += 1

print(total)
