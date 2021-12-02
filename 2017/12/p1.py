# Python 3.6.1
# Requires: networkx 1.11

import re

import networkx


def get_input():
    with open("input.txt", "r") as f:
        return [line for line in f]


def build_graph(connections):
    graph = networkx.Graph()
    r = re.compile(r"(\d{1,4}) <-> ((?:\d{1,4},? ?)+)")

    for conn in connections:
        match = r.match(conn)
        source = int(match.group(1))
        dests = [int(d) for d in match.group(2).split(", ")]
        for dest in dests:
            graph.add_edge(source, dest)

    return graph


def main():
    graph = build_graph(get_input())
    print(len(list(networkx.algorithms.dfs_preorder_nodes(graph, 0))))


if __name__ == "__main__":
    main()
