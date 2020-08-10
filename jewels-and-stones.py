"""
https://leetcode.com/problems/jewels-and-stones
"""


def jewels_stones(target: str, jewels: str) -> int:
    freq = {}
    cnt_jewel = 0
    for stone in target:
        if stone in freq:
            freq[stone] += 1
        else:
            freq[stone] = 1
    for stone in freq.keys():
        if stone in jewels:
            cnt_jewel = cnt_jewel + freq[stone]

    return cnt_jewel


if __name__ == '__main__':
    test_case = "aAAbbbb"
    jewels = "aA"
    print(f'{jewels_stones(test_case, jewels)}')