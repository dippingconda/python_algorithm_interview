"""
https://leetcode.com/problems/remove-duplicate-letters
"""
from collections import Counter


def remove_duplicate(target: str) -> str:
    counter = Counter(target)
    visited = set()
    stack = []

    for char in target:
        counter[char] -= 1
        if char in visited:
            continue
        # counter[char] 값이 > 0 이면 해당 char가 target 문자열 뒤쪽 어딘가에 아직 남아있음을 의미함.
        # 따라서, char보다 알파벳 순서가 뒤쪽이고 target 문자열 어딘가에 다시 나타날 문자는 stack과 visited에서 삭제
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            visited.remove(stack.pop())
        stack.append(char)
        visited.add(char)

    return ''.join(stack)


if __name__ == '__main__':
    test_case = ['bcabc', 'cbacdcbc']
    for tc in test_case:
        print(f'{remove_duplicate(tc)}')
