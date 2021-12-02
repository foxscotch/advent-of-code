# Python 3.6.1

import re
from collections import defaultdict, namedtuple
from datetime import datetime, timedelta


Record = namedtuple("Record", ["date", "guard", "event"])


def minutes(start, end):
    date = start
    while True:
        yield date.minute
        date = date + timedelta(minutes=1)
        if date == end:
            break


def get_input():
    input_r = re.compile(r"\[(.+)\] (.+)")
    guard_r = re.compile(r".+#(\d+)")
    date_format = "%Y-%m-%d %H:%M"

    records = []

    with open("input.txt", "r") as f:
        guard = None
        for line in f:
            match = input_r.match(line)
            record = [datetime.strptime(match[1], date_format), None, None]
            if "#" in match[2]:
                record[1] = int(guard_r.match(match[2])[1])
                record[2] = "begin"
            elif match[2] == "falls asleep":
                record[2] = "sleep"
            else:
                record[2] = "wake"
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

    guards = defaultdict(lambda: {"asleep": 0, "minutes": [0] * 60})
    sleep_time = None
    for record in input:
        if record.event == "sleep":
            sleep_time = record.date
        elif record.event == "wake":
            guards[record.guard]["asleep"] += (record.date - sleep_time).seconds // 60
            for minute in minutes(sleep_time, record.date):
                guards[record.guard]["minutes"][minute] += 1

    sleepiest, data = max(guards.items(), key=lambda r: r[1]["asleep"])
    most_common_minute = None
    minute_value = 0
    for i, times in enumerate(data["minutes"]):
        if times > minute_value:
            most_common_minute = i
            minute_value = times
    print(sleepiest * most_common_minute)


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    main()
    print(time.perf_counter() - start)
