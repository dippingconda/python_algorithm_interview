"""
https://leetcode.com/problems/maximum-subarray
"""
from typing import List


def maximum_subarr(nums: List[int]) -> int:
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0

    return max(nums)


def kadane_algo(nums: List[int]) -> int:
    MAX_INPUT_BOUNDARY = 999999999
    best_sum = -MAX_INPUT_BOUNDARY
    current_sum = 0
    for num in nums:
        current_sum = max(num, current_sum + num)
        best_sum = max(best_sum, current_sum)

    return best_sum


if __name__ == '__main__':
    test_case = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f'{kadane_algo(test_case)}')
    print(f'{maximum_subarr(test_case)}')