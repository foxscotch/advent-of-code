# Python 3.10.0


shapes = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}


def letter_to_shape(letter):
    if letter in ('A', 'X'):
        return 'rock'
    elif letter in ('B', 'Y'):
        return 'paper'
    elif letter in ('C', 'Z'):
        return 'scissors'
    else:
        raise Exception('what')


def score(left, right):
    thrown = shapes[right]

    if left == right:
        return thrown + 3
    elif left == 'scissors' and right == 'rock':
        return thrown + 6
    elif left == 'rock' and right == 'scissors':
        return thrown + 0
    else:
        return thrown + (6 if shapes[left] < shapes[right] else 0)


def get_input():
    with open("input.txt", "r") as f:
        return ((letter_to_shape(line[0]), letter_to_shape(line[-1])) for line in f.read().splitlines())


def main():
    puzzle = get_input()

    return sum(score(*match) for match in puzzle)


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
