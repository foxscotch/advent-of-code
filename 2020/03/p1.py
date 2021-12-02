# Python 3.8.3


class Repeating(list):
    def __getitem__(self, k):
        return super().__getitem__(k % len(self))


def get_input():
    with open("input.txt", "r") as f:
        return [Repeating(l) for l in f.read().split()]


def main():
    puzzle = get_input()

    trees = 0
    x = 0
    y = 0
    slope = (3, 1)

    while y < len(puzzle):
        if puzzle[y][x] == "#":
            trees += 1

        x += slope[0]
        y += slope[1]

    print(trees)


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    main()
    print(time.perf_counter() - start)
