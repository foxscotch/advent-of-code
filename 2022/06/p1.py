# Python 3.10.0


def fours(s):
    for i in range(4, len(s)):
        yield i, set(s[i-4:i])


def get_input():
    with open("input.txt", "r") as f:
        return f.read().strip()


def main():
    puzzle = get_input()

    for i, seq in fours(puzzle):
        if len(seq) == 4:
            return i


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
