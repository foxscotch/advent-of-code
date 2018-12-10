# Python 3.6.1

import re
import string
from collections import defaultdict
from functools import total_ordering
from itertools import cycle


@total_ordering
class Step:
    def __init__(self, name):
        self.name = name
        self.requires = []

    def require(self, step):
        if step not in self.requires:
            self.requires.append(step)

    def satisfy(self, step):
        if step in self.requires:
            self.requires.remove(step)

    def __repr__(self):
        return f"Step({self.name})"

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.name > other.name


class StepCollection(dict):
    def __init__(self):
        super().__init__()
        self.results = []

    def run(self):
        seconds = 0
        while True:
            for step in sorted(self.values()):
                seconds += 1

                if step in self.results:
                    continue

                if len(step.requires) == 0:
                    self.satisfy_all(step)
                    self.results.append(step)
                    if len(self.results) >= 26:
                        return ''.join([s.name for s in self.results])
                    break

    def process(self, step, requires):
        self[step].require(self[requires])

    def satisfy_all(self, required):
        for step in self.values():
            step.satisfy(required)

    def __missing__(self, key):
        self[key] = Step(key)
        return self[key]

    def __repr__(self):
        return '\n'.join([f"{x}: {x.requires}" for x in sorted(self.values())])


def get_input():
    r = re.compile(r'Step (\w) .+ step (\w)')
    with open('input.txt', 'r') as f:
        for req in f.read().strip().split('\n'):
            # (<step 1>, <requires step 2>)
            match = r.match(req)
            yield (match[2], match[1])


def main():
    steps = StepCollection()
    for step, requires in get_input():
        steps.process(step, requires)
    print(steps.run())


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    print(time.perf_counter() - start)
