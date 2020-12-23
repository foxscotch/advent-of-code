# Python 3.8.3

class Repeating(list):
    def __getitem__(self, k):
        return super().__getitem__(k % len(self))

    def pop(self, k):
        return super().pop(k % len(self))


def main():
    puzzle = Repeating([9, 4, 2, 3, 8, 7, 6, 1, 5])

    cur = puzzle[0]
    turns = 0
    while turns < 100:
        cur_index = puzzle.index(cur)

        #print(f'-- move {turns + 1} --')
        #print('cups:', str(puzzle).replace(',', '').replace(str(cur), f'({cur})')[1:-1])

        a = puzzle.pop(cur_index + 1)
        cur_index = puzzle.index(cur)
        b = puzzle.pop(cur_index + 1)
        cur_index = puzzle.index(cur)
        c = puzzle.pop(cur_index + 1)

        #print(f'pick up: {a}, {b}, {c}')

        dest = cur - 1
        while dest not in puzzle:
            if dest < min(puzzle):
                dest = max(puzzle)
            else:
                dest -= 1

        #print(f'destination: {dest}')
        #print()

        dest_index = puzzle.index(dest)
        puzzle.insert(dest_index + 1, c)
        puzzle.insert(dest_index + 1, b)
        puzzle.insert(dest_index + 1, a)

        cur = puzzle[puzzle.index(cur) + 1]

        turns += 1

    print(puzzle)


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
