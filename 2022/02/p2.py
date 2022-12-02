# Python 3.10.0


shapes = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}


def next_better(to_beat):
    if to_beat == 'rock':
        return 'paper'
    elif to_beat == 'paper':
        return 'scissors'
    else:
        return 'rock'

def next_worse(to_lose_to):
    if to_lose_to == 'rock':
        return 'scissors'
    elif to_lose_to == 'paper':
        return 'rock'
    else:
        return 'paper'

def same(to_draw_with):
    return to_draw_with


def letter_to_shape(letter):
    if letter == 'A':
        return 'rock'
    elif letter == 'B':
        return 'paper'
    elif letter == 'C':
        return 'scissors'
    else:
        raise Exception('what')


def letter_to_selector(letter):
    if letter == 'X':
        return next_worse
    elif letter == 'Y':
        return same
    elif letter == 'Z':
        return next_better
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
        return ((letter_to_shape(line[0]), letter_to_selector(line[-1])) for line in f.read().splitlines())


def main():
    puzzle = get_input()

    return sum(score(left, right(left)) for (left, right) in puzzle)


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
