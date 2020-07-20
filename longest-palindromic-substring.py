"""
https://leetcode.com/problems/longest-palindromic-substring
"""

def longestPalindromicSubstring(strs: str) -> str:
    def expand(left: int, right: int) -> str:
        while left >= 0 and right <= len(strs) and strs[left] == strs[right - 1]:
            left -= 1
            right += 1
        return strs[left + 1: right - 1]

    if len(strs) < 2 or strs == strs[::-1]:
        return strs
    result = ''
    for idx in range(len(strs) - 1):
        result = max(result, expand(idx, idx+1), expand(idx, idx+2), key=len)
    return result




if __name__ == "__main__":
    input_test = "babad"
    print(f'{longestPalindromicSubstring(input_test)}')
    input_test = "cbbd"
    print(f'{longestPalindromicSubstring(input_test)}')
