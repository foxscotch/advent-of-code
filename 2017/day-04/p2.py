# Python 3.6.1 / Official

def is_anagram(w1, w2):
    if len(w1) == len(w2):
        return sorted(w1) == sorted(w2)
    return False

with open('input.txt', 'r') as f:
    puzzle_input = []
    for line in f:
        puzzle_input.append(line.strip().split(' '))

total = 0
for phrase in puzzle_input:
    bad = False
    for i in range(len(phrase)):
        for j in range(len(phrase)):
            if i != j and is_anagram(phrase[i], phrase[j]):
                bad = True
                break
    if not bad:
        total += 1

print(total)
