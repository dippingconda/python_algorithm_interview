"""
https://leetcode.com/problems/daily-temperatures
"""
from typing import List


def daily_temp(temperatures: List[int]) -> List[int]:
    idx_stack = []
    temp_stack = []
    result = [0] * len(temperatures)
    for idx, temp in enumerate(temperatures):
        while temp_stack and temp > temp_stack[-1]:
            last_idx = idx_stack.pop()
            result[last_idx] = idx - last_idx
            temp_stack.pop()

        idx_stack.append(idx)
        temp_stack.append(temp)

    return result



if __name__ == '__main__':
    test_case = [73, 74, 75, 71, 69, 72, 76, 73]
    print(f'{daily_temp(test_case)}')