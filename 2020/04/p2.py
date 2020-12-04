# Python 3.8.3

import re


def validate_height(height):
    m = int(height[0:-2])
    unit = height[-2:]
    
    if unit == 'cm':
        return m >= 150 and m <= 193
    elif unit == 'in':
        return m >= 59 and m <= 76
    else:
        return False

required_fields = {
    'byr': lambda v: int(v) >= 1920 and int(v) <= 2002,
    'iyr': lambda v: int(v) >= 2010 and int(v) <= 2020,
    'eyr': lambda v: int(v) >= 2020 and int(v) <= 2030,
    'hgt': validate_height,
    'hcl': lambda v: re.match('#[0-9A-f]{6}', v),
    'ecl': lambda v: v in 'amb blu brn gry grn hzl oth',
    'pid': lambda v: len(v) == 9 and v.isnumeric(),
    #'cid': lambda v: True
}


def validate(passport):
    for field, validator in required_fields.items():
        if field in passport.keys():
            if not validator(passport[field]):
                return False
        else:
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
