"""
https://leetcode.com/problems/3sum
"""
from typing import List


def merge_sort(numbers: List[int]):
    if len(numbers) <= 1:
        return numbers
    mid  = len(numbers) // 2
    left_arr = numbers[:mid]
    right_arr = numbers[mid:]
    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)

    return merge(left_arr, right_arr)


def merge(left_arr: List[int], right_arr: List[int]) -> List[int]:
    len_left, len_right = len(left_arr), len(right_arr)
    result = [0] * (len_left + len_right)
    idx, left_idx, right_idx = 0, 0, 0

    while left_idx != len_left and right_idx != len_right:
        if left_arr[left_idx] <= right_arr[right_idx]:
            result[idx] = left_arr[left_idx]
            idx += 1
            left_idx += 1
        else:
            result[idx] = right_arr[right_idx]
            idx += 1
            right_idx += 1
            
    if left_idx != len_left:
        while left_idx != len_left:
            result[idx] = left_arr[left_idx]
            idx += 1
            left_idx += 1
    if right_idx != len_right:
        while right_idx != len_right:
            result[idx] = right_arr[right_idx]
            idx += 1
            right_idx += 1

    return result


def sum3(numbers: List[int]) -> List[List[int]]:
    numbers = merge_sort(numbers)
    result = []
    for idx in range(len(numbers) - 2):
        if idx > 0 and numbers[idx] == numbers[idx -1]:
            continue
        left, right = idx + 1, len(numbers) - 1
        while left < right:
            sum = numbers[idx] + numbers[left] + numbers[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                result.append([numbers[idx], numbers[left], numbers[right]])
                while left < right and numbers[left] == numbers[left + 1]:
                    left += 1
                while left < right and numbers[right] == numbers[right + 1]:
                    right -= 1
                left += 1
                right -= 1

    return result


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, 4]
    print(f'{sum3(nums)}')