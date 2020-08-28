"""
https://leetcode.com/problems/minimum-window-substring
"""


def min_window(book: str, text: str) -> str:
    import collections

    need = collections.Counter(text)
    len_text = len(text)
    left = start = end = 0

    for right, char in enumerate(book, 1):
        len_text -= need[char] > 0
        need[char] -= 1

        if len_text == 0:
            while left < right and need[book[left]] != 0:
                need[book[left]] += 1
                left += 1

            if not end or right - left <= end - start:
                start, end = left, right
            need[book[left]] += 1
            len_text += 1
            left += 1

    return book[start:end]


if __name__ == '__main__':
    S = 'ADOBECODEBANC'
    T = 'ABC'
    print(f'{min_window(S, T)}')