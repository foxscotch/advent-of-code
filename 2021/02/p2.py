# Python 3.10.0
from enum import Enum
from typing import NamedTuple


class Dir(Enum):
    F = 1
    D = 2
    U = 3


class Instruction(NamedTuple):
    direction: Dir
    distance: int


class Position(NamedTuple):
    distance: int
    depth: int
    aim: int


def get_input():
    with open("input.txt", "r") as f:
        for dir, dist in [l.split() for l in f]:
            yield Instruction(Dir[dir.upper()[0]], int(dist))


def main():
    puzzle = get_input()

    position = Position(0, 0, 0)

    for instr in puzzle:
        match instr.direction:
            case Dir.F:
                position = Position(
                    position.distance + instr.distance,
                    position.depth + position.aim * instr.distance,
                    position.aim)
            case Dir.D:
                position = Position(
                    position.distance,
                    position.depth,
                    position.aim + instr.distance)
            case Dir.U:
                position = Position(
                    position.distance,
                    position.depth,
                    position.aim - instr.distance)

    return position.distance * position.depth



if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
