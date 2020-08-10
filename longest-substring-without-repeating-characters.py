"""
https://leetcode.com/problems/longest-substring-without-repeating-characters
"""


def longest_substring(target: str) -> int:
    visited = {}
    max_len = ptr = 0
    for idx, char in enumerate(target):
        # ptr <= visited[char] 조건이 없으면
        # ptr이 후진하는 경우가 발생할 수 있음 (ptr > visited[char])
        if char in visited and ptr <= visited[char]:
            ptr = visited[char] + 1
        else:
            max_len = max(max_len, idx - ptr + 1)

        visited[char] = idx

    return max_len


if __name__ == '__main__':
    test_case = ["abcabcbb", "bbbbb", "pwwkew"]
    for tc in test_case:
        print(f'{longest_substring(tc)}')
