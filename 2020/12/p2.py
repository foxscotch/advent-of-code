# Python 3.8.3

from math import cos, sin, radians


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


class V:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rotate(self, angle):
        theta = radians(angle)
        return V(
            round(self.x * cos(theta) - self.y * sin(theta)),
            round(self.x * sin(theta) + self.y * cos(theta))
        )

    def __add__(self, other):
        if type(other) is V:
            return V(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented

    def __mul__(self, other):
        if type(other) is V:
            return V(self.x * other.x, self.y * other.y)
        elif type(other) is int:
            return V(self.x * other, self.y * other)
        else:
            return NotImplemented

    def __neg__(self):
        return V(-self.x, -self.y)

    def __str__(self):
        return f'V({self.x}, {self.y})'


class Ship:
    def __init__(self):
        self.pos = V(0, 0)
        self.waypoint = V(10, 1)
        self.direction = EAST

    def move_to_waypoint(self, distance):
        self.pos = self.pos + self.waypoint * distance

    def move_waypoint_by_coords(self, x, y):
        self.waypoint += V(x, y)

    def move_waypoint(self, distance, direction):
        direction = DIRECTIONS[direction]

        if direction == NORTH:
            self.move_waypoint_by_coords(0, distance)
        elif direction == EAST:
            self.move_waypoint_by_coords(distance, 0)
        elif direction == SOUTH:
            self.move_waypoint_by_coords(0, -distance)
        else:
            self.move_waypoint_by_coords(-distance, 0)

    def rotate_waypoint(self, degrees):
        self.waypoint = self.waypoint.rotate(degrees)


def get_input():
    with open('input.txt', 'r') as f:
        return [(s[0], int(s[1:])) for s in f.read().split()]

def main():
    puzzle = get_input()

    ship = Ship()
    for instr, i in puzzle:
        if instr in 'NESW':
            ship.move_waypoint(i, instr)
        elif instr == 'L':
            ship.rotate_waypoint(i)
        elif instr == 'R':
            ship.rotate_waypoint(-i)
        else:
            ship.move_to_waypoint(i)

    return abs(ship.pos.x) + abs(ship.pos.y)


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
