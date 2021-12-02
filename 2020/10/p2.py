# Python 3.8.3

from collections import defaultdict


def count_paths(chain):
    d = defaultdict(int)
    d[0] = 1
    for i in chain:
        d[i] = d[i - 3] + d[i - 2] + d[i - 1]
    return d[i]


def get_input():
    with open("input.txt", "r") as f:
        return set(int(i) for i in f.read().split())


def main():
    puzzle = get_input()

    d = defaultdict(int)
    d[0] = 1

    for i in puzzle:
        d[i] = d[i - 3] + d[i - 2] + d[i - 1]

    return d[i]


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
