# Python 3.6.1
# Requires: anytree 2.4.2

import re

from anytree import Node, RenderTree, PostOrderIter


def sum_weights(nodes):
    total = 0
    for node in nodes:
        if hasattr(node, 'disc_weight'):
            total += node.disc_weight
        else:
            total += node.weight
    return total

# Unused
def node_count(nodes, value):
    count = 0
    for node in nodes:
        if node.disc_weight == value:
            count += 1
    return count

# Unused
def get_different(node):
    for n in node.children:
        if node_count(n.siblings, n.disc_weight) > 0:
            if n.is_leaf:
                return n
            return get_different(n)

def main():
    with open('input.txt', 'r') as f:
        programs = {}
        for line in f:
            match = re.match(r'(\w+) \((\d+)\)(?: -> ([\w, ]+))?', line)
            if match is None:
                print('what')
            else:
                prog_name = match.group(1)
                weight = int(match.group(2))
                chstr = match.group(3)
                children = chstr.split(', ') if chstr else ()
                programs[prog_name] = (weight, children)

    nodes = {}

    for p_name, p_info in programs.items():
        nodes[p_name] = Node(p_name, weight=p_info[0])
    
    for p_name, p_node in nodes.items():
        for child in programs[p_name][1]:
            nodes[child].parent = p_node

    for program in PostOrderIter(nodes[p_name].root):
        if program.is_leaf:
            program.disc_weight = program.weight
        else:
            program.disc_weight = program.weight + sum_weights(program.children)

    with open('output.txt', 'w+', encoding='utf8') as f:
        for pre, _, node in RenderTree(nodes[p_name].root):
            f.write(f'{pre}{node}\n')

    print('Please inspect output.txt to find the answer.')


if __name__ == '__main__':
    main()
