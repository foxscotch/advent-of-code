# Python 3.8.3

import re


field_pattern = re.compile(r"([A-z ]+): (\d+)-(\d+) or (\d+)-(\d+)")


def check_value(value, fields):
    for field, ((amin, amax), (bmin, bmax)) in fields.items():
        if amin <= value <= amax or bmin <= value <= bmax:
            # print('valid', value, f'[{field} {amin}-{amax} / {bmin}-{bmax}]')
            yield field
        else:
            # print('invalid', value, f'[{field} {amin}-{amax} / {bmin}-{bmax}]')
            yield False


def check_ticket(ticket, fields):
    return all(any(check_value(value, fields)) for value in ticket)


def get_input():
    with open("input.txt", "r") as f:
        fields = {}
        mine = None
        tickets = []

        lines = iter(f.read().splitlines())
        for line in lines:
            m = field_pattern.match(line)
            if m:
                name, amin, amax, bmin, bmax = m.groups()
                fields[name] = (int(amin), int(amax)), (int(bmin), int(bmax))
            elif line.startswith("your"):
                mine = [int(i) for i in next(lines).split(",")]
            elif len(line) > 0 and line[0].isnumeric():
                tickets.append([int(i) for i in line.split(",")])

        return fields, mine, tickets


def main():
    fields, mine, tickets = get_input()
    tickets = [t for t in tickets if check_ticket(t, fields)]

    possible_fields = [set(fields.keys()) for _ in range(len(mine))]
    for position, possible in enumerate(possible_fields):
        ticket_sets = []
        for ticket in tickets:
            value = ticket[position]
            ticket_sets.append(set(check_value(value, fields)))
            print(f"{position} valid fields: {ticket_sets[-1]}")
        print(
            f"{position} possibilities: {ticket_sets[0] & ticket_sets[1] & ticket_sets[2]}"
        )

    print(possible_fields)


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
