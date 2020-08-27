"""
https://leetcode.com/problems/sliding-window-maximum
"""
from typing import List


def max_sliding_window(nums: List[int], width: int) -> List[int]:
    from collections import deque

    result = []
    window = deque()
    current_max = float('-inf')

    for idx, val in enumerate(nums):
        window.append(val)

        if idx < width - 1:
            continue

        if current_max == float('-inf'):
            current_max = max(window)
        elif val > current_max:
            current_max = val

        result.append(current_max)

        if current_max == window.popleft():
            current_max = float('-inf')

    return result



if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(f'{max_sliding_window(nums, k)}')