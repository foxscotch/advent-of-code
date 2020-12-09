# Python 3.8.3

from itertools import combinations


def check(check, target):
    for i in check:
        if target - i in check and target - i != i:
            return True
    return False

def find_invalid(l):
    preamble_length = 25

    for i in range(preamble_length, len(l)):
        prev = set(l[i-preamble_length:i])
        
        if not check(prev, l[i]):
            return l[i]

def get_input():
    with open('input.txt', 'r') as f:
        return [int(i) for i in f.read().split()]

def main():
    puzzle = get_input()

    invalid = find_invalid(puzzle)
    #print(f'invalid={invalid}')

    for i in range(len(puzzle)):
        running_sum = 0
        for j in range(i, len(puzzle)):
            #print(f'i={i} p[i]={puzzle[i]}, j={j} p[j]={puzzle[j]}')
            running_sum += puzzle[j]
            if running_sum > invalid:
                #print(running_sum, 'greater!')
                break
            elif running_sum == invalid:
                sum_range = puzzle[i:j+1]
                #print(running_sum, f'{min(sum_range) + max(sum_range)}', sum_range)
                return min(sum_range) + max(sum_range)


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
