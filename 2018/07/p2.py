# Python 3.6.1

import re
import string
import time
from collections import defaultdict
from functools import total_ordering
from itertools import cycle


@total_ordering
class Step:
    def __init__(self, name):
        self.name = name
        self.work_remaining = ord(name) - 64 + 60
        self.requires = []

    def ready(self):
        return len(self.requires) == 0

    def finished(self):
        return self.work_remaining == 0

    def work(self):
        if self.work_remaining > 0:
            self.work_remaining -= 1

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


class Worker:
    cur_id = 0

    def __init__(self, steps):
        self.steps = steps
        self.current_step = None
        self.finished = False
        self.id = Worker.cur_id
        Worker.cur_id += 1

    def work(self):
        if self.current_step is None:
            if not self.get_next():
                return

        self.current_step.work()
        if self.current_step.finished():
            self.steps.satisfy_all(self.current_step)
            self.get_next()

    def get_next(self):
        for step in self.steps.values():
            if step.ready() and step not in self.steps.results:
                self.current_step = step
                self.steps.results.append(step)
                return True
        self.finished = True
        return False


class StepCollection(dict):
    def __init__(self, worker_count):
        super().__init__()
        self.results = []
        self.workers = [Worker(self) for i in range(worker_count)]

    def run(self):
        seconds = 0
        while True:
            seconds += 1
            for worker in self.workers:
                worker.work()
            if self.all_finished():
                return seconds

    def all_finished(self):
        return False not in [w.finished for w in self.workers]

    def process(self, step, requires):
        self[step].require(self[requires])

    def satisfy_all(self, required):
        for step in self.values():
            step.satisfy(required)

    def __missing__(self, key):
        self[key] = Step(key)
        return self[key]

    def __repr__(self):
        return "\n".join([f"{x}: {x.requires}" for x in sorted(self.values())])


def get_input():
    r = re.compile(r"Step (\w) .+ step (\w)")
    with open("input.txt", "r") as f:
        for req in f.read().strip().split("\n"):
            # (<step 1>, <requires step 2>)
            match = r.match(req)
            yield (match[2], match[1])


def main():
    steps = StepCollection(5)
    for step, requires in get_input():
        steps.process(step, requires)
    print(steps.run())


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    main()
    print(time.perf_counter() - start)
