# Python 3.8.3

def get_input():
    with open('input.txt', 'r') as f:
        return [s.split() for s in f.read().split('\n\n')]

def main():
    puzzle = get_input()
    print(sum(len(s) for s in [{q for l in p for q in l} for p in puzzle]))


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    print(time.perf_counter() - start)
