"""
https://leetcode.com/problems/product-of-array-except-self
"""
from typing import List

def product_of_array_except_self(arr: List[int]) -> List[int]:
    prev = 1
    result = []
    for val in arr:
        result.append(prev)
        prev = val * prev
    print(result)
    prev = 1
    for idx in range(len(arr) - 1, -1, -1):
        result[idx] = result[idx] * prev
        prev = arr[idx] * prev

    return result




if __name__ == '__main__':
    input_arr = [1, 2, 3, 4]
    print(f'{product_of_array_except_self(input_arr)}')