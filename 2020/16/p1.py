# Python 3.8.3

import re


field_pattern = re.compile(r'([A-z ]+): (\d+)-(\d+) or (\d+)-(\d+)')

def check_value(value, fields):
    for field, ((amin, amax), (bmin, bmax)) in fields.items():
        if amin <= value <= amax or bmin <= value <= bmax:
            #print('valid', value, f'[{field} {amin}-{amax} / {bmin}-{bmax}]')
            return True
    #print('invalid', value)
    return False

def check_ticket(ticket, fields):
    total = 0
    for value in ticket:
        if not check_value(value, fields):
            total += value
            break
    return total

def get_input():
    with open('input.txt', 'r') as f:
        fields = {}
        mine = None
        tickets = []

        lines = iter(f.read().splitlines())
        for line in lines:
            m = field_pattern.match(line)
            if m:
                name, amin, amax, bmin, bmax = m.groups()
                fields[name] = (int(amin), int(amax)), (int(bmin), int(bmax))
            elif line.startswith('your'):
                mine = [int(i) for i in next(lines).split(',')]
            elif len(line) > 0 and line[0].isnumeric():
                tickets.append([int(i) for i in line.split(',')])

        return fields, mine, tickets

def main():
    fields, mine, tickets = get_input()
    return sum([check_ticket(ticket, fields) for ticket in tickets])


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
