"""
https://leetcode.com/problems/intersection-of-two-arrays
"""
from typing import List, Set


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1) & set(nums2))


def solution(nums1: List[int], nums2: List[int]) -> List[int]:
    result: Set = set()

    nums1.sort()
    nums2.sort()

    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] > nums2[j]:
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            result.add(nums1[i])
            i += 1
            j += 1

    return list(result)


if __name__ == '__main__':
    nums_1 = [1, 2, 2, 1]
    nums_2 = [2, 2]
    print(f'{intersection(nums_1, nums_2)}')
    print(f'{solution(nums_1, nums_2)}')
    nums_1 = [4, 9, 5]
    nums_2 = [9, 4, 9, 8, 4]
    print(f'{intersection(nums_1, nums_2)}')
    print(f'{solution(nums_1, nums_2)}')
