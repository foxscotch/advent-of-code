# Python 3.8.3

import re


pattern = re.compile("(\d+)-(\d+) (\w): (\w+)")


def get_input():
    pwds = []
    with open("input.txt", "r") as f:
        for p in f.read().strip().split("\n"):
            m = pattern.match(p)
            pwds.append((int(m[1]), int(m[2]), m[3], m[4]))
    return pwds


def main():
    puzzle = get_input()
    count = 0

    for p1, p2, letter, pwd in puzzle:
        if (pwd[p1 - 1] == letter) != (pwd[p2 - 1] == letter):
            count += 1

    print(count)


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    main()
    print(time.perf_counter() - start)
