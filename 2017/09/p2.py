# Python 3.6.1
# Requires: anytree 2.4.2

from anytree import AnyNode as Node, PreOrderIter


def get_input():
    with open("input.txt", "r") as f:
        return f.read()


def get_score(text):
    score = 0
    with open("input.txt", "r") as f:
        i = 0
        garbage = False
        while True:
            if i == len(text):
                break
            char = text[i]

            if not garbage and char == "<":
                garbage = True
            elif garbage and char == ">":
                garbage = False
            elif garbage and char == "!":
                i += 1
            elif garbage:
                score += 1

            i += 1
    return score


def main():
    print(get_score(get_input()))


if __name__ == "__main__":
    main()
