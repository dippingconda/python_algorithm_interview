"""
https://leetcode.com/problems/binary-search
"""
from typing import List


def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    mid = left + (right - left) // 2

    while left <= right:
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid

        mid = left + (right - left) // 2

    return -1



if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(f'{search(nums, target)}')