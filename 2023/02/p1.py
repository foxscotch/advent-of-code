# Python 3.12.0

from enum import Enum
from typing import Generator


LIMITS = { 'red': 12, 'green': 13, 'blue': 14 }


class Sample:
    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        return f'Sample(r={self.red}, g={self.green}, b={self.blue})'

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

    def possible(self):
        red_ok = max(sample.red for sample in self.samples) <= LIMITS['red']
        green_ok = max(sample.green for sample in self.samples) <= LIMITS['green']
        blue_ok = max(sample.blue for sample in self.samples) <= LIMITS['blue']

        return red_ok and green_ok and blue_ok


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
        if game.possible():
            sum += game.id

    return sum


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
