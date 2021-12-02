# Python 3.8.3


def get_input():
    with open("input.txt", "r") as f:
        return [s.split() for s in f.read().split("\n\n")]


def main():
    groups = get_input()
    questions_by_group = [{q for l in p for q in l} for p in groups]

    total = 0
    for group, questions in zip(groups, questions_by_group):
        for question in questions:
            if all([question in g for g in group]):
                total += 1

    print(total)


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    main()
    print(time.perf_counter() - start)
