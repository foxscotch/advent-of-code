# Python 3.8.3


class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class CircularLinkedList:
    def __init__(self, l):
        self.start = Node(l[0])
        prev = self.start

        n = None
        for item in l[1:]:
            n = Node(item, prev=prev)
            prev.next = n
            prev = n

        self.end = n
        self.start.prev = self.end
        self.end.next = self.start

    def __getitem__(self, k):
        i = 0
        n = self.start
        while i < k:
            n = n.next
            i += 1
        return n.value

    def __iter__(self):
        n = self.start
        while n != self.end:
            yield n.value
            n = n.next
        yield n.value


def main():
    puzzle = CircularLinkedList("I", [9, 4, 2, 3, 8, 7, 6, 1, 5])
    # puzzle += list(range(max(puzzle), 1_000_001))

    cur = puzzle[0]
    turns = 0
    while turns < 1_000_000:
        cur_index = puzzle.index(cur)

        # print(f'-- move {turns + 1} --')
        # print('cups:', str(puzzle).replace(',', '').replace(str(cur), f'({cur})')[1:-1])

        a = puzzle.pop(cur_index + 1)
        cur_index = puzzle.index(cur)
        b = puzzle.pop(cur_index + 1)
        cur_index = puzzle.index(cur)
        c = puzzle.pop(cur_index + 1)

        # print(f'pick up: {a}, {b}, {c}')

        dest = cur - 1
        while dest not in puzzle:
            if dest < min(puzzle):
                dest = max(puzzle)
            else:
                dest -= 1

        # print(f'destination: {dest}')
        # print()

        dest_index = puzzle.index(dest)
        puzzle.insert(dest_index + 1, c)
        puzzle.insert(dest_index + 1, b)
        puzzle.insert(dest_index + 1, a)

        cur = puzzle[puzzle.index(cur) + 1]

        turns += 1

    # print(puzzle)


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
