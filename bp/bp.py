# Python 3.12.0


import typing


def get_input() -> list[str]:
    with open("input.txt", "r") as f:
        return f.read().split()


def main() -> typing.Any:
    puzzle = get_input()

    # Code here


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
