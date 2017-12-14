# Python 3.6.1

import re


class Firewall:
    def __init__(self, layers):
        super(Firewall, self).__init__()
        self.pos = 0
        for layer in layers:


class Layer:
    def __init__(self, range):
        self.list = [False] * range
        self.list[0] = True
        self.pos = 0

        self.moving_down = True

    def move(self):
        if self.moving_down:
            self.pos += 1
        else:
            self.pos -= 1

        if self.pos in (0, self.range - 1):
            self.moving_down = not self.moving_down


def get_input():
    r = re.compile(r'(\d{1,2}): (\d{1,2})').match
    with open('input.txt', 'r') as f:
        return [(int(r(l).group(1)), int(r(l).group(2))) for l in f]

def main():
    print(get_input())


if __name__ == '__main__':
    main()
