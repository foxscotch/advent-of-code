# Python 3.8.3

import re


required_fields = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    #'cid'
]


def validate(passport):
    for field in required_fields:
        if field not in passport.keys():
            return False
    return True

def get_input():
    with open('input.txt', 'r') as f:
        lists = [re.split('\s+', s.strip()) for s in f.read().split('\n\n')]
        return [{k: v for k,v in [s.split(':') for s in l]} for l in lists]

def main():
    puzzle = get_input()
    count = 0

    for passport in puzzle:
        if validate(passport):
            count += 1
    
    print(count)


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    print(time.perf_counter() - start)
