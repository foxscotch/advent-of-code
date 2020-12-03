# Python 3.8.3

from collections import defaultdict


def get_input():
    with open('input.txt', 'r') as f:
        wires = f.read().split()
        return wires[0].split(','), wires[1].split(',')

def main():
    wires = get_input()

    positions = defaultdict(lambda: [False, False])

    for wire in wires:
        pos = (0, 0)
        for instr in wire:
            dir = instr[0]
            dist = int(instr[1:])

            for i in range(dist):
                if dir == 'L':
                    pos = (pos[0] - 1, pos[1])
                if dir == 'R':
                    pos = (pos[0] + 1, pos[1])
                if dir == 'U':
                    pos = (pos[0], pos[1] - 1)
                if dir == 'D':
                    pos = (pos[0], pos[1] + 1)
                
                if wire is wires[0]:
                    positions[pos][0] = True
                else:
                    positions[pos][1] = True
    
    minimum = 9999999999  # it is what it is

    for pos, [a, b] in positions.items():
        if a and b:
            dist = abs(pos[0]) + abs(pos[1])
            if dist < minimum:
                minimum = dist
    
    print(minimum)


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    print(time.perf_counter() - start)
