"""
https://leetcode.com/problems/permutations
"""
from typing import List


def permutation(nums: List[int], r: int):
    result = []
    used = [False] * len(nums)

    def dfs(chosen: List[int], used: List[bool]):
        if len(chosen) == r:
            result.append(chosen[:])
            return

        for i in range(len(nums)):
            if not used[i]:
                chosen.append(nums[i])
                used[i] = True
                dfs(chosen, used)
                used[i] = False
                chosen.pop()

    dfs([], used)
    return result


def solution(nums: List[int]) -> List[List[int]]:
    result = []
    prev_element = []

    def dfs(element: List[int]):
        if len(element) == 0:
            result.append(prev_element[:])

        for e in element:
            next_element = element[:]
            next_element.remove(e)
            prev_element.append(e)
            dfs(next_element)
            prev_element.pop()
    dfs(nums)
    return result


if __name__ == '__main__':
    test_case = [1, 2, 3]
    print(f'{permutation(test_case, 1)}')
    print(f'{solution(test_case)}')