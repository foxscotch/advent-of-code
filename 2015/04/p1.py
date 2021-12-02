import hashlib


puzzle_input = b"iwrupvqb"
number = 100000

while True:
    key = puzzle_input + str(number).encode()
    if hashlib.md5(key).hexdigest()[:5] == "00000":
        break
    number += 1

print(number)

# Runs way faster than I expected, lol
