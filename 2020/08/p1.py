# Python 3.8.3

def get_input():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        return [(s.split()[0], int(s.split()[1])) for s in lines]

def main():
    puzzle = get_input()
    
    acc = 0
    id = 0
    ids_run = set()
    while id not in ids_run:
        ids_run.add(id)
        instr, amt = puzzle[id]

        if instr == 'acc':
            acc += amt
        
        id += amt if instr == 'jmp' else 1
    
    print(acc)


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    print(time.perf_counter() - start)
