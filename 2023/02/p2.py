# Python 3.12.0

from dataclasses import dataclass
from enum import Enum
from typing import Generator


LIMITS = { 'red': 12, 'green': 13, 'blue': 14 }


@dataclass
class Sample:
    red: int
    green: int
    blue: int

    @classmethod
    def parse(cls, string: str):
        colors = [s.split() for s in string.split(', ')]

        red = 0
        green = 0
        blue = 0

        for color in colors:
            match color:
                case [count, 'red']:
                    red += int(count)
                case [count, 'green']:
                    green += int(count)
                case [count, 'blue']:
                    blue += int(count)

        return cls(red, green, blue)


class Game:
    def __init__(self, idx: int, samples: list[Sample]):
        self.id = idx
        self.samples = samples

    def __repr__(self):
        return f'Game(id={self.id}, possible={self.possible()}, samples={self.samples})'

    def minimum_power(self):
        red_max = max(sample.red for sample in self.samples)
        green_max = max(sample.green for sample in self.samples)
        blue_max = max(sample.blue for sample in self.samples)

        return red_max * green_max * blue_max


def get_input() -> Generator[Game, None, None]:
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

        for line in lines:
            game, raw_samples = line.split(': ')

            game_id = int(game.split()[1])
            samples = [Sample.parse(s) for s in raw_samples.split('; ')]

            yield Game(game_id, samples)


def main():
    puzzle = get_input()

    sum = 0

    for game in puzzle:
        sum += game.minimum_power()

    return sum


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
