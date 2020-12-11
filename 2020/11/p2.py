# Python 3.8.3

FL = -1
EM = 0
OC = 1

CHECK_LOCATIONS = (
    (-1, -1), (0, -1), (1, -1),
    (-1,  0),          (1,  0),
    (-1,  1), (0,  1), (1,  1),
)


class GY(list):
    def __getitem__(self, k):
        if k < 0:
            return GX([EM])

        try:
            return super().__getitem__(k)
        except IndexError:
            return GX([EM])
    
    def __str__(self):
        return '\n'.join(str(g) for g in self)


class GX(list):
    def __getitem__(self, k):
        if k < 0:
            return EM

        try:
            return super().__getitem__(k)
        except IndexError:
            return EM

    def __str__(self):
        s = ''
        for i in self:
            s += 'L' if i == EM else ('.' if i == FL else '#')
        return s


def check_surrounding(x, y, grid):
    total = 0

    for fx, fy in CHECK_LOCATIONS:
        i = 0
        while True:
            i += 1
            v = grid[y + fy*i][x + fx*i]
            if v is OC:
                total += 1
                break
            elif v is EM:
                break
    
    return total

def get_input():
    with open('input.txt', 'r') as f:
        lines = f.read().split()
        return GY([GX([EM if s == 'L' else FL for s in l]) for l in lines])

def main():
    grid = get_input()
    
    changed = False
    while True:
        changed = False
        new_grid = GY([GX(g.copy()) for g in grid])

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                surrounding = check_surrounding(x, y, grid)
                if grid[y][x] == EM and surrounding == 0:
                    new_grid[y][x] = OC
                    changed = True
                elif grid[y][x] == OC and surrounding >= 5:
                    new_grid[y][x] = EM
                    changed = True
        
        grid = new_grid

        if not changed:
            break
    
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == OC:
                count += 1
    return count


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
