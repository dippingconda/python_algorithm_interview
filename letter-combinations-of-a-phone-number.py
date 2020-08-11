"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number
"""
from typing import Dict, List

'''
키패드에서 키를 2개 누른 경우가 아니면 동작하지 않음
def combination(keypad: Dict, select: str) -> List[str]:
    result = []
    for i in keypad[select[0]]:
        for j in keypad[select[1]]:
            result.append(''.join([i, j]))
    return result
'''


def combination(selected: str) -> List[str]:
    result = []

    def dfs(idx: int, comb: str):
        if comb.__len__() == selected.__len__():
            result.append(comb)
            return

        for letter in keypad[selected[idx]]:
            dfs(idx + 1, comb + letter)

    if not selected:
        return []

    dfs(0, '')

    return result


def solution(selected: str) -> List[str]:
    def dfs(index: int, path: str):
        if len(path) == len(selected):
            result.append(path)
            return

        for i in range(index, len(selected)):
            for j in keypad[selected[i]]:
                dfs(i + 1, path + j)

    result = []

    if not selected:
        return []

    dfs(0, '')
    return result


if __name__ == '__main__':
    keypad = {'2': ['a', 'b', 'c'],
              '3': ['d', 'e', 'f'],
              '4': ['g', 'h', 'i'],
              '5': ['j', 'k', 'l'],
              '6': ['m', 'n', 'o'],
              '7': ['p', 'q', 'r', 's'],
              '8': ['t', 'u', 'v'],
              '9': ['w', 'x', 'y', 'z'],
              }
    test_case = '23'
    print(f'{combination(test_case)}')
    print(f'{solution(test_case)}')
    test_case = '234'
    print(f'{combination(test_case)}')
    print(f'{solution(test_case)}')
    test_case = ''
    print(f'{combination(test_case)}')
    print(f'{solution(test_case)}')
