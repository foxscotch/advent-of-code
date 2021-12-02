# Python 3.8.3

from functools import reduce


def absolute_modulo(a, b):
    return ((a % b) + b) % b


def inverse_modulo(a, mod):
    b = a % mod
    for i in range(mod):
        if (b * i) % mod == 1:
            return i
    return 1


def chinese_remainder(buses):
    N = reduce(lambda acc, x: acc * x if x else acc, buses)

    def reducer(acc, cur):
        i, cur = cur
        if not cur:
            return acc

        a = absolute_modulo(cur - i, cur)
        nU = N // cur
        inverse = inverse_modulo(nU, cur)
        return acc + (a * nU * inverse)

    return reduce(reducer, enumerate(buses), 0) % N


def get_input():
    with open("input.txt", "r") as f:
        lines = f.read().split()
        return [int(i) if i.isnumeric() else 0 for i in lines[1].split(",")]


def main():
    bus_ids = get_input()
    return round(chinese_remainder(bus_ids))


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
