# Python 3.8.3


def get_input():
    with open("input.txt", "r") as f:
        return set(int(i) for i in f.read().split())


def main():
    puzzle = get_input()

    last_joltage = 0
    one_jolt = 0
    three_jolts = 1
    while len(puzzle) != 0:
        if last_joltage + 1 in puzzle:
            last_joltage = last_joltage + 1
            one_jolt += 1
        elif last_joltage + 2 in puzzle:
            last_joltage = last_joltage + 2
        elif last_joltage + 3 in puzzle:
            last_joltage = last_joltage + 3
            three_jolts += 1
        puzzle.remove(last_joltage)

    print(one_jolt, three_jolts)
    return one_jolt * three_jolts


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
