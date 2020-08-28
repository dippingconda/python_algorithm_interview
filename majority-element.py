"""
https://leetcode.com/problems/majority-element
"""
from typing import List


def dynamic_programming(nums: List[int]) -> int:
    cnt = {}
    half = len(nums) // 2
    for num in nums:
        if num not in cnt:
            cnt[num] = 1
        else:
            cnt[num] += 1

        if cnt[num] > half:
            return num


def divide_conquer(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    half = len(nums) // 2
    a = divide_conquer(nums[:half])
    b = divide_conquer(nums[half:])

    return [b, a][nums.count(a) > half]


def sorting(nums: List[int]) -> int:
    return sorted(nums)[len(nums) // 2]


if __name__ == '__main__':
    test_case = [1, 2, 1, 3, 1, 4, 1, 1]
    print(f'{dynamic_programming(test_case)}')
    print(f'{divide_conquer(test_case)}')
    print(f'{sorting(test_case)}')