# Python 3.6.1

import re
from pdb import set_trace


class Firewall:
    def __init__(self, layers):
        self.pos = -1
        self.penalty = 0
        self.caught = False

        self.layers = [None for i in range(layers[-1][0] + 1)]
        for layer in layers:
            self.layers[layer[0]] = Layer(layer[1])

    def move(self):
        for _ in range(len(self.layers)):
            self.move_once()

    def move_with_delay(self, delay):
        for _ in range(delay):
            self.move_scanners()
        self.move()

    def move_once(self):
        self.move_packet()

        layer = self.layers[self.pos]
        if type(layer) is Layer:
            if layer.pos == 0:
                self.penalty += self.pos * layer.range
                self.caught = True

        self.move_scanners()

    def move_packet(self):
        self.pos += 1

    def move_scanners(self):
        for layer in self.layers:
            if layer is not None:
                layer.move_scanner()


class Layer:
    def __init__(self, range):
        self.range = range
        self.pos = 0

        self.moving_down = True

    def move_scanner(self):
        if self.moving_down:
            self.pos += 1
        else:
            self.pos -= 1

        if self.pos == 0 or self.pos == self.range - 1:
            self.moving_down = not self.moving_down

    def __repr__(self):
        return f"Layer({len(self.list)})"


def get_input():
    r = re.compile(r"(\d{1,2}): (\d{1,2})").match
    with open("input.txt", "r") as f:
        return [(int(r(l).group(1)), int(r(l).group(2))) for l in f]


def main():
    inp = get_input()

    delay = 0
    while True:
        f = Firewall([(0, 3), (1, 2), (4, 4), (6, 4)])
        f = Firewall(inp)
        f.move_with_delay(delay)
        print(delay)
        if f.caught:
            delay += 1
        else:
            break

    print(delay)


if __name__ == "__main__":
    main()
