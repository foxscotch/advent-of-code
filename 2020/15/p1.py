# Python 3.8.3

from collections import defaultdict


class Tracker:
    def __init__(self, puzzle):
        self.numbers = defaultdict(lambda: (0, 0))
        self.turn = 1

        for n in puzzle:
            print(f'Turn {self.turn}: speaking {n}')
            self.numbers[n] = (self.turn, 1)
            self.turn += 1

        self.last = n

    def run(self, turns):
        while self.turn <= turns:
            if self.last in self.numbers:
                last_turn, how_many = self.numbers[self.last]
                if how_many > 1:
                    self.speak(self.turn - last_turn, how_many)
                else:
                    self.speak(0, how_many)
            else:
                self.speak(0)
            self.turn += 1

    def speak(self, n, spoken=0):
        print(f'Turn {self.turn}: speaking {n}, last was {self.last} on turn {self.numbers[self.last]}')
        self.last = n
        self.numbers[n] = (self.turn, spoken + 1)


def main():
    puzzle = [14, 8, 16, 0, 1, 17]
    puzzle = [0, 3, 6]
    t = Tracker(puzzle)
    return t.run(10)


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
