# Python 3.10.0

class Grid(list):
    def new_row(self):
        self.append([])

    def new_col(self, row, value=None):
        self[row].append(value)

    def __getitem__(self, index):
        if isinstance(index, tuple):
            return self[index[1]][index[0]]
        else:
            return super().__getitem__(index)


def get_input():
    with open("input.txt", "r") as f:
        map = Grid()
        start = None
        destination = None

        input_rows = f.read().split()

        for y, row in enumerate(input_rows):
            map.new_row()

            for x, col in enumerate(row):
                if col == 'S':
                    start = x, y
                    map.new_col(y, 1)
                elif col == 'E':
                    destination = x, y
                    map.new_col(y, 26)
                else:
                    map.new_col(y, ord(col) - 96)

        return start, destination, map




def main():
    start, destination, map = get_input()

    for row in map:
        print(''.join(chr(r + 96) for r in row))


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
