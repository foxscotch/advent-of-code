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

    most_series = list(puzzle)
    least_series = list(puzzle)

    oxy_rating = None
    co2_rating = None

    for i in range(len(puzzle[0])):
        if oxy_rating is not None and co2_rating is not None:
            break

        m, l = get_most_common_value([s[i] for s in most_series])

        most_series = list(filter(lambda num: num[i] == m, most_series))
        if len(most_series) == 1:
            oxy_rating = most_series[0]

        m, l = get_most_common_value([s[i] for s in least_series])

        least_series = list(filter(lambda num: num[i] == l, least_series))
        if len(least_series) == 1:
            co2_rating = least_series[0]

    return int(oxy_rating, 2) * int(co2_rating, 2)


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
