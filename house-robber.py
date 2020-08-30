"""
https://leetcode.com/problems/house-robber
"""
from typing import List


def rob(nums: List[int]) -> int:
    global dp
    if not nums:
        return 0

    if len(nums) <= 2:
        return max(nums)

    dp[0], dp[1] = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    return dp[-1]


if __name__ == '__main__':
    test_case = [1, 2, 3, 1]
    dp = [0] * len(test_case)
    print(f'{rob(test_case)}')
    test_case = [2, 7, 9, 3, 1]
    dp = [0] * len(test_case)
    print(f'{rob(test_case)}')
