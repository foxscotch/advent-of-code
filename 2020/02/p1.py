# Python 3.8.3

import re
from collections import Counter


pattern = re.compile("(\d+)-(\d+) (\w): (\w+)")


def get_input():
    pwds = []
    with open("input.txt", "r") as f:
        for p in f.read().strip().split("\n"):
            m = pattern.match(p)
            pwds.append((int(m[1]), int(m[2]), m[3], Counter(m[4])))
    return pwds


def main():
    puzzle = get_input()
    count = 0

    for min, max, letter, pwd in puzzle:
        quantity = pwd[letter]
        if quantity >= min and quantity <= max:
            count += 1

    print(count)


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    main()
    print(time.perf_counter() - start)
