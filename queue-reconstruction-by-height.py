"""
https://leetcode.com/problems/queue-reconstruction-by-height
"""
from typing import List


def reconstruct_queue(people: List[List[int]]) -> List[List[int]]:
    import heapq

    result = []
    max_heap = []
    for height, cnt_taller in people:
        heapq.heappush(max_heap, [-height, cnt_taller])

    while max_heap:
        height, cnt_taller = heapq.heappop(max_heap)
        print(height, cnt_taller)
        result.insert(cnt_taller, [-height, cnt_taller])

    return result


if __name__ == '__main__':
    test_case = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    print(f'{reconstruct_queue(test_case)}')