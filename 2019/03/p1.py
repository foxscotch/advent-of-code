# Python 3.8.3

def get_input():
    with open('input.txt', 'r') as f:
        wires = f.read().split()
        return wires[0].split(','), wires[1].split(',')

def main():
    w1, w2 = get_input()
    
    w1_pos = (0, 0)
    w2_pos = (0, 0)
    w1_locations = []
    shared_locations = []

    for instr in w1:
        dir = instr[0]
        dist = int(instr[1:])


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    print(time.perf_counter() - start)
