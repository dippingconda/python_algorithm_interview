"""
https://leetcode.com/problems/reverse-string
"""
from typing import List


def reverseString(in_str: str) -> None:
    start = 0
    end = len(in_str) - 1
    while start < end:
        in_str[end], in_str[start] = in_str[start], in_str[end]
        start += 1
        end -= 1
    print(f'reverse 1: {input_str}')

def reverseString2(in_str: List[str]) -> None:
    in_str.reverse()
    print(f'reverse 2: {input_str}')

def reverseString3(in_str: List[str]) -> None:
    in_str[:] = in_str[::-1]
    print(f'reverse 3: {input_str}')

if __name__ == "__main__":
    strs = "hello"
    input_str = [str(char) for char in strs]
    print(f'original input : {input_str}')
    reverseString(input_str)
    reverseString2(input_str)
    reverseString3(input_str)
