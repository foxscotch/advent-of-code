# Python 3.6.1

def opposite(a, b):
    if a.isupper() and a.lower() == b:
        return True
    elif a.islower() and a.upper() == b:
        return True
    else:
        return False

def get_input():
    with open('input.txt', 'r') as f:
        return list(f.read().strip())

def main():
    input = get_input()

    removed = True
    while removed:
        removed = False
        i = 1  # Starting at 1 intentionally, to compare the first two letters
        while True:
            if i >= len(input):
                break

            a = input[i - 1]
            b = input[i]

            if opposite(a, b):
                removed = True
                del input[i-1:i+1]
            else:
                i += 1

    print(len(input))


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    print(time.perf_counter() - start)
