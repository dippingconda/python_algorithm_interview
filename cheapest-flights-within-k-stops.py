"""
https://leetcode.com/problems/cheapest-flights-within-k-stops
"""
from typing import List


def find_cheapest_price(n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    import heapq
    graph = {}
    for u, v, w in flights:
        if u not in graph:
            graph[u] = [(v, w)]
        else:
            graph[u].append((v, w))

    queue = [(0, src, K)]

    while queue:
        price, node, k = heapq.heappop(queue)
        if node == dst:
            return price
        if k >= 0:
            for v, w in graph[node]:
                cost = price + w
                heapq.heappush(queue, (cost, v, k - 1))

    return -1


if __name__ == '__main__':
    num_stops = 3
    edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src, dst, K = 0, 2, 0
    print(f'{find_cheapest_price(num_stops, edges, src, dst, K)}')