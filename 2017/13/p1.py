# Python 3.6.1

import re
from pdb import set_trace


class Firewall:
    def __init__(self, layers):
        self.pos = -1
        self.penalty = 0

        self.layers = [None for i in range(layers[-1][0] + 1)]
        for layer in layers:
            self.layers[layer[0]] = Layer(layer[1])

    def move(self):
        for _ in range(len(self.layers)):
            self.move_once()

    def move_once(self):
        self.move_packet()

        layer = self.layers[self.pos]
        if type(layer) is Layer:
            if layer.pos == 0:
                self.penalty += self.pos * len(layer.list)

        self.move_scanners()

    def move_packet(self):
        self.pos += 1

    def move_scanners(self):
        for layer in self.layers:
            if type(layer) is Layer:
                layer.move_scanner()


class Layer:
    def __init__(self, range):
        self.list = [0] * range
        self.list[0] = 1
        self.pos = 0

        self.moving_down = True

    def move_scanner(self):
        self.list[self.pos] = 0

        if self.moving_down:
            self.pos += 1
        else:
            self.pos -= 1

        self.list[self.pos] = 1

        if self.pos in (0, len(self.list) - 1):
            self.moving_down = not self.moving_down

    def __repr__(self):
        return f"Layer({len(self.list)})"


def get_input():
    r = re.compile(r"(\d{1,2}): (\d{1,2})").match
    with open("input.txt", "r") as f:
        return [(int(r(l).group(1)), int(r(l).group(2))) for l in f]


def main():
    f = Firewall(get_input())
    # f = Firewall([(0, 3), (1, 2), (4, 4), (6, 4)])
    f.move()
    print(f.penalty)


if __name__ == "__main__":
    main()
