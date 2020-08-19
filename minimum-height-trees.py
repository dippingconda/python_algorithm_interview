"""
https://leetcode.com/problems/minimum-height-trees
"""
from typing import List, Dict


def find_min_height_trees(n: int, edges: List[List[int]]) -> List[int]:
    if n <= 1:
        return edges

    graph = {}
    leaves = []
    for u, v in edges:
        if u not in graph:
            graph[u] = [v]
        else:
            graph[u].append(v)
        if v not in graph:
            graph[v] = [u]
        else:
            graph[v].append(u)

    for i in graph.keys():
        if len(graph[i]) == 1:
            leaves.append(i)

    while n > 2:
        n -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)

            if len(graph[neighbor]) == 1:
                new_leaves.append(neighbor)

        leaves = new_leaves

    return leaves


if __name__ == '__main__':
    n = 4
    edges = [[1, 0], [1, 2], [1, 3]]
    print(f'{find_min_height_trees(n, edges)}')
    n = 6
    edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
    print(f'{find_min_height_trees(n, edges)}')
