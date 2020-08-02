"""
https://leetcode.com/problems/array-partition-i
"""
from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)
    return merge(left, right)


def merge(left_arr: List[int], right_arr: List[int]) -> List[int]:
    len_left, len_right = len(left_arr), len(right_arr)
    left_idx, right_idx, idx = 0, 0, 0
    result = [0] * (len_left + len_right)
    while left_idx != len_left and right_idx != len_right:
        if left_arr[left_idx] <= right_arr[right_idx]:
            result[idx] = left_arr[left_idx]
            idx += 1
            left_idx += 1
        else:
            result[idx] = right_arr[right_idx]
            idx += 1
            right_idx += 1
    while left_idx != len_left:
        result[idx] = left_arr[left_idx]
        idx += 1
        left_idx += 1
    while right_idx != len_right:
        result[idx] = right_arr[right_idx]
        idx += 1
        right_idx += 1

    return result


def array_partition_i(arr: List[int]) -> int:
    arr = merge_sort(arr)
    result = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            result += arr[i]

    return result


if __name__ == "__main__":
    input_arr = [1, 4, 3, 2]
    print(f'{array_partition_i(input_arr)}')
