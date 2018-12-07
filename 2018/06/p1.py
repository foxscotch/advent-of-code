# Python 3.6.1

from random import randrange


class Location:
    def __init__(self, x, y):
        self.id = randrange(2**16)

    def __repr__(self):
        return f'Location({self.id:0>4x})'


def get_input():
    with open('input.txt', 'r') as f:
        for coordinate in f.read().strip().split('\n'):
            coords = coordinate.split(', ')
            yield int(coords[0]), int(coords[1])

def main():
    input = get_input()

    grid = {}
    for x, y in input:
        grid[x, y] = Location(x, y)

    print(grid)


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    print(time.perf_counter() - start)
