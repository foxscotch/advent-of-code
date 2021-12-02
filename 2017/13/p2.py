# Python 3.6.1

import re
import sys
from pdb import set_trace


"""
This version is significantly faster than p2_slow.py. I don't think you could
reasonably ever reach the answer for this using that one. Anyway, for this one,
I took an approach where I _calculate_ the 'position' of the scanner in the
current row. I think it's pretty neat. Probably could've thought about it
sooner, and made p1 faster too, but oh well. Still, cool. Way faster. It does
still take a while though. I might see if I can think of a way to speed it up
even more, sometime.

I just kept the slow version for posterity.
"""


class Firewall:
    def __init__(self, layers):
        self.pos = -1
        self.penalty = 0
        self.caught = False

        self.layers = [None for i in range(layers[-1][0] + 1)]
        for layer in layers:
            self.layers[layer[0]] = (layer[1] - 1) * 2

    def move(self, step=1):
        for _ in range(len(self.layers)):
            self.pos += 1
            self.move_once(step)
            step += 1

    def move_once(self, step):
        layer = self.layers[self.pos]
        if layer is not None:
            if step % layer == 1:
                self.penalty += self.pos * (layer // 2 + 1)
                self.caught = True

    def reset(self):
        self.pos = -1
        self.penalty = 0
        self.caught = False

    def __repr__(self):
        return f"Firewall({self.pos}, {self.penalty}, {self.caught})"


def get_input():
    r = re.compile(r"(\d{1,2}): (\d{1,2})").match
    with open("input.txt", "r") as f:
        return [(int(r(l).group(1)), int(r(l).group(2))) for l in f]


def main():
    inp = get_input()
    f = Firewall(inp)

    delay = 0
    while True:
        f.move(delay + 1)
        if f.caught:
            delay += 1
            f.reset()
        else:
            break

    print(delay)


if __name__ == "__main__":
    main()
