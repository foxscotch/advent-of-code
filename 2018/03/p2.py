# Python 3.6.1

import re
from collections import namedtuple


Claim = namedtuple('Claim', ['id', 'x', 'y', 'w', 'h'])


def get_input():
    r = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
    input = []
    with open('input.txt', 'r') as f:
        for line in f:
            match = r.match(line)
            input.append(Claim(int(match[1]),
                               int(match[2]),
                               int(match[3]),
                               int(match[4]),
                               int(match[5])))
    return input

def print_grid(grid):
    for row in grid:
        print(' '.join((str(v) for v in row)))

def main(dim=1000):
    input = get_input()
    grid = [[0 for j in range(dim)] for i in range(dim)]

    for claim in input:
        for y in range(claim.y, claim.y + claim.h):
            for x in range(claim.x, claim.x + claim.w):
                grid[y][x] += 1

    # Check for a claim with no overlap. Probably not a very efficient way to do
    # this, but as long as it works. :)
    no_overlap = None
    for claim in input:
        no_overlap = claim
        for y in range(claim.y, claim.y + claim.h):
            for x in range(claim.x, claim.x + claim.w):
                if grid[y][x] > 1:
                    no_overlap = None
        if no_overlap is not None:
            break
    print(no_overlap.id)


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    print(time.perf_counter() - start)
