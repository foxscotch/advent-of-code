# Python 3.8.3

from math import ceil



def departures(i):
    last = 0
    while True:
        last = last + i
        yield last

def check_departure(time, bus_id):
    if time == 0:
        return True
    return time % bus_id == 0

def get_input():
    with open('input.txt', 'r') as f:
        lines = f.read().split()
        return [int(i) if i.isnumeric() else 0 for i in lines[1].split(',')]

def main():
    bus_ids = get_input()

    maximum = max(bus_ids)
    max_position = bus_ids.index(maximum)

    for i in departures(max(bus_ids)):
        position = 0
        time = i - max_position
        for bus_id in bus_ids:
            if bus_id == 0:
                position += 1
            elif time % bus_id == 0:
                position += 1
            else:
                break
            time += 1
        if position == len(bus_ids):
            return i - max_position


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
