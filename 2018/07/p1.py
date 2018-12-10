# Python 3.6.1

import re
import string
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
        super().__init__({l: Step(l) for l in string.ascii_uppercase})
        self.results = []

    def run(self):
        while True:
            for step in self.values():
                if step in self.results:
                    continue

                if len(step.requires) == 0:
                    self.satisfy_all(step)
                    self.results.append(step)
                    if len(self.results) >= 26:
                        return ''.join([s.name for s in self.results])
                    break

    def satisfy_all(self, required):
        for step in self.values():
            step.satisfy(required)

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
        steps.get(step).require(steps.get(requires))
    print(steps.run())


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    print(time.perf_counter() - start)
