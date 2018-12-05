# Python 3.6.1

import re
from collections import namedtuple
from datetime import datetime


Record = namedtuple('Record', ['date', 'guard', 'event'])


def get_input():
    input_r = re.compile(r'\[(.+)\] (.+)')
    guard_r = re.compile(r'.+#(\d+)')
    date_format = '%Y-%m-%d %H:%M'

    records = []

    with open('input.txt', 'r') as f:
        guard = None
        for line in f:
            match = input_r.match(line)
            record = [datetime.strptime(match[1], date_format), None, None]
            if '#' in match[2]:
                record[1] = int(guard_r.match(match[2])[1])
                record[2] = 'begin'
            elif match[2] == 'falls asleep':
                record[2] = 'sleep'
            else:
                record[2] = 'wake'
            records.append(record)
        records.sort(key=lambda r: r[0])

    guard = None
    real_records = []
    for record in records:
        if record[1] is not None:
            guard = record[1]
        real_records.append(Record(record[0], guard, record[2]))
    return real_records

def main():
    input = get_input()

    # Guard objects:
    #   <guard id>: {
    #       asleep: <minutes spent sleeping>,
    #       minutes: [
    #           <times asleep during 0th minute>,
    #           <times asleep during 1st minute>,
    #           <times asleep during 2nd minute>,
    #           ...
    #           <times asleep during 59th minute>
    #       ]
    #   }
    guards = {}
    status = 'awake'
    for record in input:
        pass


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    print(time.perf_counter() - start)
