# Python 3.8.3

def get_input():
    with open('input.txt', 'r') as f:
        return f.read().split()

def main():
    puzzle = get_input()
    # Code here


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
