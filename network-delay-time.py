"""
https://leetcode.com/problems/network-delay-time
"""
from typing import List


def network_delay_time(times: List[List[int]], N: int, K: int) -> int:
    import heapq
    graph = {}
    for u, v, w in times:
        if u not in graph:
            graph[u] = [(v, w)]
        else:
            graph[u].append((v, w))

    queue = [(0, K)]
    dist = {}

    while queue:
        time, node = heapq.heappop(queue)
        if node not in dist:
            dist[node] = time
            if node in graph:
                for v, w in graph[node]:
                    cost = time + w
                    heapq.heappush(queue, (cost, v))

    if len(dist) == N:
        return max(dist.values())
    return -1




if __name__ == '__main__':
    topology = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    num_node, start_node = 4, 2
    print(f'{network_delay_time(topology, num_node, start_node)}')