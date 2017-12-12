# Python 3.6.1
# Requires: anytree 2.4.2

from anytree import AnyNode as Node, PreOrderIter


def get_input():
    groups = ''
    with open('input.txt', 'r') as f:
        i = 0
        stream = f.read()
        garbage = False
        while True:
            if i == len(stream):
                break
            char = stream[i]

            if not garbage and char == '<':
                garbage = True
            elif garbage and char == '>':
                garbage = False
            elif garbage and char == '!':
                i += 1
            elif not garbage and char != ',':
                groups += char

            i += 1
    return groups

def build_tree(groups):
    root = Node()
    parent = root
    for char in groups[1:-1]:
        if char == '{':
            node = Node()
            node.parent = parent
            parent = node
        elif char == '}':
            parent = parent.parent
    return root

def score_tree(tree):
    score = 0
    for node in PreOrderIter(tree):
        score += node.depth + 1
    return score

def main():
    tree = build_tree(get_input())
    print(score_tree(tree))


if __name__ == '__main__':
    main()
