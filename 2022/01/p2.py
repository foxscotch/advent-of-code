# Python 3.10.0


def get_input():
    with open("input.txt", "r") as f:
        return f.read().splitlines()


def main():
    puzzle = get_input()

    elves = []
    current = 0

    for calories in puzzle:
        if calories == '':
            elves.append(current)
            current = 0
            continue

        current += int(calories)

    return sum(sorted(elves, reverse=True)[0:3])



if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
