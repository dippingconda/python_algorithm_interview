"""
https://leetcode.com/problems/group-anagrams
"""
from typing import List
import re


def groupAnagrams1(words: List[str]) -> List[List[str]]:
    anagrams = {}
    for word in words:
        anagram_key = "".join(sorted(word))
        if anagram_key not in anagrams:
            anagrams[anagram_key] = [word]
        else:
            anagrams[anagram_key].append(word)

    result = [anagram for anagram in anagrams.values()]
    return result


def groupAnagrams2(strs: List[str]) -> List[List[str]]:
    import collections
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return anagrams.values()


if __name__ == "__main__":
    input_str = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f'result : {groupAnagrams1(input_str)}')
    print(f'result : {groupAnagrams2(input_str)}')
    print(f'{groupAnagrams1(input_str) == groupAnagrams2(input_str)}')
