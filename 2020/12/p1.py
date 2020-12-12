# Python 3.8.3

NORTH = 0
EAST = 90
SOUTH = 180
WEST = 270

DIRECTIONS = {
    'N': NORTH,
    'E': EAST,
    'S': SOUTH,
    'W': WEST
}


class Ship:
    def __init__(self):
        self.pos = (0, 0)
        self.direction = EAST

    def move_by_coordinates(self, x, y):
        self.pos = (self.pos[0] + x, self.pos[1] + y)

    def move(self, distance, direction=None):
        if direction is None:
            direction = self.direction
        else:
            direction = DIRECTIONS[direction]

        if direction == NORTH:
            self.move_by_coordinates(0, distance)
        elif direction == EAST:
            self.move_by_coordinates(distance, 0)
        elif direction == SOUTH:
            self.move_by_coordinates(0, -distance)
        else:
            self.move_by_coordinates(-distance, 0)

    def turn_right(self, degrees):
        self.direction = (self.direction + degrees) % 360

    def turn_left(self, degrees):
        self.turn_right(-degrees)


def get_input():
    with open('input.txt', 'r') as f:
        return [(s[0], int(s[1:])) for s in f.read().split()]

def main():
    puzzle = get_input()

    ship = Ship()
    for instr, i in puzzle:
        if instr in 'NESW':
            ship.move(i, instr)
        elif instr == 'L':
            ship.turn_left(i)
        elif instr == 'R':
            ship.turn_right(i)
        else:
            ship.move(i)

    x, y = ship.pos
    return abs(x) + abs(y)


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
