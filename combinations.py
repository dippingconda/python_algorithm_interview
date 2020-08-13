"""
https://leetcode.com/problems/combinations
"""
from typing import List


def combinations(n: int, k: int) -> List[List[int]]:
    result = []

    def dfs(elements: List[int], start: int):
        if len(elements) == k:
            result.append(elements[:])
            return

        for i in range(start, n + 1):
            elements.append(i)
            dfs(elements, i + 1)
            elements.pop()

    dfs([], 1)

    return result


def solution(n: int, k: int) -> List[List[int]]:
    result = []

    def dfs(elements: List[int], start: int, k: int):
        if k == 0:
            result.append(elements[:])
            return

        for i in range(start, n + 1):
            elements.append(i)
            dfs(elements, i + 1, k - 1)
            elements.pop()

    dfs([], 1, k)

    return result


if __name__ == '__main__':
    test_case = {'n': 4, 'k': 2}
    print(f"{combinations(test_case['n'], test_case['k'])}")
    print(f"{solution(test_case['n'], test_case['k'])}")