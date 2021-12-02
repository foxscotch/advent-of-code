# Python 3.8.3

FLOOR = -1
EMPTY = 0
OCCUPIED = 1

CHECK_LOCATIONS = (
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
)


class G(dict):
    def __missing__(self, k):
        return EMPTY


def check_surrounding(x, y, grid):
    total = 0

    for fx, fy in CHECK_LOCATIONS:
        i = 0
        while True:
            i += 1
            v = grid[x + fx * i, y + fy * i]
            if v is OCCUPIED:
                total += 1
                break
            elif v is EMPTY:
                break

    return total


def get_input():
    with open("input.txt", "r") as f:
        d = G()
        for i, line in enumerate(f.read().split()):
            for j, char in enumerate(line):
                d[j, i] = EMPTY if char == "L" else FLOOR
        return d


def main():
    grid = get_input()

    changed = False
    while True:
        changed = False
        new_grid = G(grid.copy())

        for (x, y), chair in grid.items():
            surrounding = check_surrounding(x, y, grid)
            if chair is EMPTY and surrounding == 0:
                new_grid[x, y] = OCCUPIED
                changed = True
            elif grid[x, y] is OCCUPIED and surrounding >= 5:
                new_grid[x, y] = EMPTY
                changed = True

        grid = new_grid

        if not changed:
            break

    count = 0
    for (x, y), chair in grid.items():
        if grid[x, y] is OCCUPIED:
            count += 1
    return count


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
