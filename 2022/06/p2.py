# Python 3.10.0


def fourteens(s):
    for i in range(14, len(s)):
        yield i, set(s[i-14:i])


def get_input():
    with open("input.txt", "r") as f:
        return f.read().strip()


def main():
    puzzle = get_input()

    for i, seq in fourteens(puzzle):
        if len(seq) == 14:
            return i


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
