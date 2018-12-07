# Python 3.6.1

import string


def opposite(a, b):
    if a.isupper() and a.lower() == b:
        return True
    elif a.islower() and a.upper() == b:
        return True
    else:
        return False

def react(l):
    l = list(l)

    i = 1  # Starting at 1 intentionally, to compare the first two letters
    while True:
        if i >= len(l):
            break

        a = l[i - 1]
        b = l[i]

        if opposite(a, b):
            del l[i]
            del l[i-1]
            i -= 1
        else:
            i += 1

    return len(l)

def get_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()

def main():
    input = get_input()

    shortest = len(input)
    for char in string.ascii_lowercase:
        result = react(input.replace(char, '').replace(char.upper(), ''))
        if result < shortest:
            shortest = result
    print(shortest)


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    print(time.perf_counter() - start)
