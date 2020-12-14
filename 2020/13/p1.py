# Python 3.8.3

from math import ceil


def get_input():
    with open('input.txt', 'r') as f:
        lines = f.read().split()
        earliest = int(lines[0])
        ids = lines[1].split(',')
        return earliest, [int(i) for i in ids if i.isnumeric()]

def main():
    earliest_time, bus_ids = get_input()

    departure_times = {}
    for bus_id in bus_ids:
        wait = ceil(earliest_time / bus_id) * bus_id - earliest_time
        departure_times[wait] = bus_id
    
    shortest_wait = min(departure_times.keys())
    return shortest_wait * departure_times[shortest_wait]


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
