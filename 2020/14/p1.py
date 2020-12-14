# Python 3.8.3

import re


pattern = re.compile(r'(mask|mem)(?:\[(\d+)\])? = (.+)')


def apply_mask(value, mask):
    for i, bit in enumerate(reversed(mask)):
        if bit == '1':
            value |= (1 << i)
        elif bit == '0':
            value &= ~(1 << i)
    return value

def get_input():
    with open('input.txt', 'r') as f:
        for line in f.read().splitlines():
            type, addr, value = pattern.match(line).groups()
            if addr:
                yield type, (int(addr), int(value))
            else:
                yield type, value

def main():
    puzzle = get_input()

    memory = {}
    mask = None

    for type, value in puzzle:
        if type == 'mask':
            mask = value
        else:
            addr, value = value
            memory[addr] = apply_mask(value, mask)

    return sum(memory.values())


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
