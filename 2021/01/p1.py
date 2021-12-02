# Python 3.10.0


def get_input():
    with open("input.txt", "r") as f:
        return [int(i) for i in f.read().split()]


def main():
    puzzle = get_input()

    count = 0
    prev = puzzle[0]

    for depth in puzzle[1:]:
        if depth > prev:
            count += 1
        prev = depth

    return count


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
