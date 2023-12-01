# Python 3.12.0

import re
from collections import defaultdict


class dd(defaultdict):
    def __missing__(self, k):
        return k


digits = dd()
digits['one'] = '1'
digits['two'] = '2'
digits['three'] = '3'
digits['four'] = '4'
digits['five'] = '5'
digits['six'] = '6'
digits['seven'] = '7'
digits['eight'] = '8'
digits['nine'] = '9'

regex = re.compile(rf"(?=((\d|{'|'.join(digits.keys())})))")


def get_input():
    with open("input.txt", "r") as f:
        return f.read().split()

def components(s):
    return [digits[i.group(1)] for i in regex.finditer(s)]

def main():
    puzzle = get_input()

    return sum(int(i[0] + i[-1]) for i in (components(s) for s in puzzle))



if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
