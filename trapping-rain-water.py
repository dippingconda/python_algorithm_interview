"""
https://leetcode.com/problems/trapping-rain-water
"""
from typing import List


def trapping_rain_water(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    volume = 0

    while left < right:
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
        left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
    return volume


if __name__ == '__main__':
    wall = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(f'{trapping_rain_water(wall)}')

