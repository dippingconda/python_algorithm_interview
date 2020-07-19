"""
https://leetcode.com/problems/valid-palindrome
"""
def IsPalindrome1(in_str: str) -> bool:
    from collections import  deque
    strs = deque()

    for char in in_str:
        if char.isalnum():
            strs.append(char.lower())
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True

def IsPalindrome2(in_str: str) -> bool:
    strs = []
    for char in in_str:
        if char.isalnum():
            strs.append(char.lower())

    return strs == strs[::-1]

if __name__ == '__main__':
    input_str = 'A man, a plan, a canal: Panama'
    print(f'first method : {IsPalindrome1(input_str)}')
    print(f'second method : {IsPalindrome2(input_str)}')
