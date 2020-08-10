"""
https://leetcode.com/problems/top-k-frequent-elements
"""
from typing import List


def top_k(target: List[int], freq: int) -> int:
    from collections import Counter
    count = Counter(target)
    result = []

    for key in count:
        if count[key] >= freq:
            result.append(key)

    return result


def solution(target: List[int], k: int) -> int:
    import heapq
    from collections import Counter
    heap = []
    count = Counter(target)
    # heapq는 min-heap임
    # max-heap 대신 heap에 음수 값으로 넣음으로써
    # pop 시 최빈값이 나오도록 함
    for cnt in count:
        # heappush 함수는 push 시 매번 heapify를 수행하여 push함
        heapq.heappush(heap, (-count[cnt], cnt))

    result = []
    for _ in range(k):
        result.append(heapq.heappop(heap)[1])

    return result


if __name__ == '__main__':
    test_case = [1, 1, 1, 2, 2, 3]
    k = 2
    print(f'{top_k(test_case, k)}')
    print(f'{solution(test_case, k)}')
