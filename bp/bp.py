# Python 3.6.1

def get_input():
    with open('input.txt', 'r') as f:
        return f.read().split()

def main():
    input = get_input()
    # Code here


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    print(time.perf_counter() - start)
