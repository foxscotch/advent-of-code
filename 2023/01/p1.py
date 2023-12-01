# Python 3.12.0

from re import sub


def get_input():
    with open("input.txt", "r") as f:
        return f.read().split()


def main():
    puzzle = get_input()

    return sum(int(i[0] + i[-1]) for i in (sub(r'\D', '', s) for s in puzzle))


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
