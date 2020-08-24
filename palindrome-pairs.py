"""
https://leetcode.com/problems/palindrome-pairs
"""
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_id = -1
        self.palindrome_word_ids = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word[::] == word[::-1]

    def insert(self, index: int, word: str) -> None:
        node = self.root
        for i, char in enumerate(reversed(word)):
        #for i, char in enumerate(word[::-1]):
            if self.is_palindrome(word[0: len(word) - i]):
                node.palindrome_word_ids.append(index)
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.word_id = index

    def search(self, index: int, word: str) -> List[List[int]]:
        result = []
        node = self.root

        # 판별 로직 1
        while word:
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])

            if word[0] not in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]

        # 판별 로직 2
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])

        # 판별 로직 3
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])

        return result


def palindrome_pairs(words: List[str]) -> List[List[int]]:
    trie = Trie()

    for i, word in enumerate(words):
        trie.insert(i, word)

    result = []
    for i, word in enumerate(words):
        result.extend(trie.search(i, word))

    return result

if __name__ == '__main__':
    test_case = ['abcd', 'dcba', 'lls', 's', 'sssll']
    print(f'{palindrome_pairs(test_case)}')
