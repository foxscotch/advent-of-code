# Python 3.8.3

from itertools import combinations


def check(check, target):
    for i in check:
        if target - i in check and target - i != i:
            return True
    return False

def get_input():
    with open('input.txt', 'r') as f:
        return [int(i) for i in f.read().split()]

def main():
    puzzle = get_input()
    
    preamble_length = 25

    for i in range(preamble_length, len(puzzle)):
        prev = set(puzzle[i-preamble_length:i])
        
        if not check(prev, puzzle[i]):
            return puzzle[i]


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
