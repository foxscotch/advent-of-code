# Python 3.10.0


def get_input():
    with open("input.txt", "r") as f:
        return [int(i) for i in f.read().split()]


def windows(input):
    position = 0

    while len(input) - position:
        yield sum(input[position : position + 3])
        position += 1


def main():
    puzzle = windows(get_input())

    count = 0
    prev = next(puzzle)

    for depth in puzzle:
        if depth > prev:
            count += 1
        prev = depth

    return count


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
