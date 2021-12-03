# Python 3.10.0


def get_input():
    with open("input.txt", "r") as f:
        return f.read().split()


def get_most_common_value(bits):
    count_of_ones = sum(int(i) for i in bits)
    count_of_zeroes = len(bits) - count_of_ones
    return ("1", "0") if count_of_ones >= count_of_zeroes else ("0", "1")


def main():
    puzzle = get_input()

    gamma = ""
    epsilon = ""

    for i in range(len(puzzle[0])):
        g, e = get_most_common_value([s[i] for s in puzzle])
        gamma += g
        epsilon += e

    return int(gamma, 2) * int(epsilon, 2)


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
