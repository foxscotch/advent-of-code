# Python 3.8.3
# Requires: regex 2020.11.13, networkx 2.5

import regex
import networkx


pattern = regex.compile(r'^(\w+ \w+) bags contain (?:(\d+ \w+ \w+) bags?(?:, )?)*')


def must_contain(bag_name, graph):
    # Return count of bags that must be contained by bags of type bag_name
    total = 0
    for successor in graph.successors(bag_name):
        count = graph[bag_name][successor]['count']
        total += count
        total += must_contain(successor, graph) * count
    return total

def process_line(line):
    m = pattern.match(line)
    return m.group(1), [(int(s.split(' ', 1)[0]), s.split(' ', 1)[1]) for s in m.captures(2)]

def get_input():
    with open('input.txt', 'r') as f:
        lines = [process_line(l) for l in f.read().splitlines()]
        graph = networkx.DiGraph()
        for container, contained_tuples in lines:
            for count, contained in contained_tuples:
                graph.add_edge(container, contained, count=count)
        return graph

def main():
    puzzle = get_input()
    print(must_contain('shiny gold', puzzle))


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    print(time.perf_counter() - start)
