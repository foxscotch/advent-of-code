import hashlib


puzzle_input = b"iwrupvqb"
number = 100000

while True:
    key = puzzle_input + str(number).encode()
    if hashlib.md5(key).hexdigest()[:6] == "000000":
        break
    number += 1

print(number)

# Now that I think about it, starting with 100,000 was probably not the right
# thing to do. I could've easily never found my answer. But I did, and I guess
# it probably saved a little time. So okay.
